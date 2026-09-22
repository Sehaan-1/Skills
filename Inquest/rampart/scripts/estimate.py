#!/usr/bin/env python3
"""Back-of-the-envelope capacity estimator for the rampart skill (system design).

Stdlib only. Round aggressively — order-of-magnitude answers are the point.

Examples:
  estimate.py full --reads-month 100000000 --writes-month 10000000 \
      --record-bytes 1300 --read-bytes 5000
  estimate.py qps --requests-month 2500000000 --peak-factor 3
  estimate.py storage --records-month 10000000 --record-bytes 1300 --years 3
  estimate.py shards --total-tb 450 --node-capacity-gb 100 --headroom 2
"""
from __future__ import annotations

import argparse
import math
import sys

SECONDS_PER_MONTH = 2_500_000  # primer's conversion guide


def human(n: float) -> str:
    for unit, div in (("TB", 1e12), ("GB", 1e9), ("MB", 1e6), ("KB", 1e3)):
        if abs(n) >= div:
            return f"{n / div:,.1f} {unit}"
    return f"{n:,.0f} bytes"


def qps(requests_month: float, peak_factor: float) -> None:
    avg = requests_month / SECONDS_PER_MONTH
    print(f"requests/month : {requests_month:,.0f}")
    print(f"avg QPS        : {avg:,.1f}")
    print(f"peak QPS       : {avg * peak_factor:,.1f}  (×{peak_factor:g} peak factor)")


def storage(records_month: float, record_bytes: float, years: float) -> None:
    per_month = records_month * record_bytes
    per_year = per_month * 12
    total = per_year * years
    print(f"record size    : {record_bytes:,.0f} B ({human(record_bytes)})")
    print(f"new data/month : {human(per_month)}")
    print(f"new data/year  : {human(per_year)}")
    print(f"{years:g}-year total : {human(total)}")


def shards(total_tb: float, node_capacity_gb: float, headroom: float) -> None:
    usable_gb = node_capacity_gb * headroom  # headroom > 1 keeps peaks safe
    need = (total_tb * 1024) / usable_gb
    print(f"cluster raw    : {total_tb:g} TB")
    print(f"node budget    : {node_capacity_gb:g} GB usable ×{headroom:g} headroom"
          f" = {usable_gb:g} GB effective per node")
    print(f"nodes/shards   : {math.ceil(need)}  (rounded up)")


def bandwidth(reads_month: float, read_bytes: float) -> None:
    bytes_month = reads_month * read_bytes
    bps = bytes_month * 8 / (SECONDS_PER_MONTH)  # bits/s average
    print(f"read payload   : {read_bytes:,.0f} B/response")
    print(f"avg egress     : {human(bytes_month)}/month ≈ {human(bytes_month / SECONDS_PER_MONTH)}/s"
          f" ≈ {bps / 1e6:,.1f} Mbps")


def full(args: argparse.Namespace) -> None:
    print("== QPS ==")
    qps(args.reads_month + args.writes_month, args.peak_factor)
    print(f"reads/s  avg   : {args.reads_month / SECONDS_PER_MONTH:,.1f}"
          f"  peak {args.reads_month / SECONDS_PER_MONTH * args.peak_factor:,.1f}")
    print(f"writes/s avg   : {args.writes_month / SECONDS_PER_MONTH:,.1f}"
          f"  peak {args.writes_month / SECONDS_PER_MONTH * args.peak_factor:,.1f}")
    print("\n== Storage ==")
    storage(args.writes_month, args.record_bytes, args.years)
    if args.read_bytes:
        print("\n== Bandwidth ==")
        bandwidth(args.reads_month, args.read_bytes)
    if args.node_capacity_gb:
        total_tb = (args.writes_month * args.record_bytes * 12 * args.years) / 1e12
        print("\n== Shards ==")
        shards(total_tb, args.node_capacity_gb, args.headroom)
    print("\nReminder: reads usually >> writes (10:1–1000:1); design the read path first.")


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)

    f = sub.add_parser("full", help="one-shot: QPS + storage + optional bandwidth/shards")
    f.add_argument("--reads-month", type=float, required=True)
    f.add_argument("--writes-month", type=float, required=True)
    f.add_argument("--record-bytes", type=float, required=True, help="avg stored size per write")
    f.add_argument("--read-bytes", type=float, default=0, help="avg response size on read path")
    f.add_argument("--peak-factor", type=float, default=2.5)
    f.add_argument("--years", type=float, default=3)
    f.add_argument("--node-capacity-gb", type=float, default=0, help="set to enable shard count")
    f.add_argument("--headroom", type=float, default=2.0, help="capacity headroom multiplier")
    f.set_defaults(func=full)

    q = sub.add_parser("qps", help="requests/month → avg & peak QPS")
    q.add_argument("--requests-month", type=float, required=True)
    q.add_argument("--peak-factor", type=float, default=2.5)
    q.set_defaults(func=lambda a: qps(a.requests_month, a.peak_factor))

    s = sub.add_parser("storage", help="records/month → storage growth")
    s.add_argument("--records-month", type=float, required=True)
    s.add_argument("--record-bytes", type=float, required=True)
    s.add_argument("--years", type=float, default=3)
    s.set_defaults(func=lambda a: storage(a.records_month, a.record_bytes, a.years))

    h = sub.add_parser("shards", help="total data → node/shard count")
    h.add_argument("--total-tb", type=float, required=True)
    h.add_argument("--node-capacity-gb", type=float, required=True)
    h.add_argument("--headroom", type=float, default=2.0)
    h.set_defaults(func=lambda a: shards(a.total_tb, a.node_capacity_gb, a.headroom))

    b = sub.add_parser("bandwidth", help="reads/month → egress")
    b.add_argument("--reads-month", type=float, required=True)
    b.add_argument("--read-bytes", type=float, required=True)
    b.set_defaults(func=lambda a: bandwidth(a.reads_month, a.read_bytes))

    args = p.parse_args()
    args.func(args)
    return 0


if __name__ == "__main__":
    sys.exit(main())
