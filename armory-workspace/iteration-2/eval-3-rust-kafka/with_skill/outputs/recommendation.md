# SDK Recommendation: high-throughput Kafka consumer (~200k msg/s) — Rust/Actix-web

**Top pick: `rdkafka` (MIT, v0.39.0)** — Rust bindings over librdkafka, the C engine Confluent maintains; it is the only candidate here with a credible claim to your throughput target.

## Why it wins

- **Performance 5/5** — librdkafka is the reference high-throughput Kafka client. The rust-rdkafka README publishes ~1M msg/s produce throughput on decade-old laptop hardware (with `BaseProducer`, localhost broker) — your 200k msg/s consume target is comfortably within its envelope. Architecturally: a C core doing the I/O and batching, with a Rust layer exposing a safe async `Stream` — no pure-Rust client currently matches that pipeline.
- **Maintenance 4/5** — v0.39.0 published 2026-01-25 (live crates.io data), ~37M all-time downloads, ~6.7M in the last quarter. Release cadence is measured in months, not weeks, but the project has run since 2016 and leans on Confluent-maintained librdkafka underneath.
- **License 5/5** — MIT (verified live), no gate for any project type.
- **DX 4/5** — `StreamConsumer`/`FutureProducer` integrate directly with tokio (what Actix-web runs on), docs.rs documentation, well-trodden patterns for at-least-once delivery and offset management.

## Comparison

Weights: **40% performance / 20% each other** — you declared performance the top priority.

| Candidate | Performance | Maintenance | License | DX | Weighted |
|---|---|---|---|---|---|
| `rdkafka` | 5/5 | 4/5 | ✅ MIT | 4/5 | **4.6/5** |
| `kafka` (kafka-rust, pure Rust) | 2/5 | 1/5 | ✅ MIT OR Apache-2.0 | 2/5 | **2.4/5** |

Facts live-verified on crates.io 2026-09-22: `kafka` last shipped 0.10.0 on **2023-09-24** — three years without a release, ~145k recent downloads vs rdkafka's 6.7M. Considered and dropped: there is no `confluent-kafka` Rust crate — Confluent's distribution for Rust is librdkafka-based, which is exactly what rdkafka wraps.

## Trade-offs

- **Native build dependency is the real cost**: rdkafka compiles/links librdkafka. The `cmake-build` feature builds it from source (needs CMake + a C toolchain in CI); `dynamic-linking` uses the system library instead. Either way your build graph is no longer pure Rust, and builds are slower. That's the tax for the C engine's speed.
- **FFI surface** — rare librdkafka bugs or config quirks surface through the bindings; debugging occasionally drops you into C-level config strings (`"fetch.min.bytes"` etc.).
- Choosing `kafka` (kafka-rust) would give a pure-Rust build but costs everything else: unmaintained for 3 years, missing modern broker features, realistically short of 200k msg/s. If a no-C build graph is a hard requirement, the better move is still rdkafka with `dynamic-linking` against a packaged librdkafka.

## Getting started

```toml
# Cargo.toml
[dependencies]
rdkafka = { version = "0.39", features = ["cmake-build"] }
tokio = { version = "1", features = ["macros", "rt-multi-thread"] }
futures = "0.3"
```

```rust
use futures::StreamExt;
use rdkafka::config::ClientConfig;
use rdkafka::consumer::{Consumer, StreamConsumer};

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let consumer: StreamConsumer = ClientConfig::new()
        .set("bootstrap.servers", "kafka-1:9092,kafka-2:9092")
        .set("group.id", "ingest-service")
        .set("enable.auto.commit", "false")     // commit after processing -> at-least-once
        .set("auto.offset.reset", "earliest")
        .create()?;

    consumer.subscribe(&["events"])?;

    let mut stream = consumer.stream();
    while let Some(result) = stream.next().await {
        let msg = result?;
        // hot path: process msg.payload()
        // then commit offsets (store_offset + commit) once processed
    }
    Ok(())
}
```

## Assumptions & caveats

- Assumed a tokio-compatible async runtime (Actix-web's runtime is tokio-based, so `StreamConsumer` fits; consume in a spawned task, not inside request handlers).
- 200k msg/s assumed across the topic's partitions — you'll want enough partitions/consumers to parallelize; that's broker topology, not an SDK choice.
- Throughput claims for rdkafka come from its own README benchmarks (producer-side, localhost); treat consume-side headroom as architectural reasoning, not a measured guarantee. Plan a load test for at-scale tuning (fetch sizes, batching).
