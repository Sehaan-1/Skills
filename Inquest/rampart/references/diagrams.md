# Diagram snippet library (mermaid)

Paste-ready patterns for `design`/`review` modes. Adapt names; keep labels short. Pair every added box with its trade-off in prose.

## 1. Basic 3-tier + cache (starting point for most drills)

```mermaid
flowchart LR
    C[Client] --> CDN[CDN]
    CDN --> LB[L7 load balancer]
    LB --> W1[Web / reverse proxy]
    LB --> W2[Web / reverse proxy]
    W1 --> A[App servers - stateless]
    W2 --> A
    A --> CA[(Cache\ncache-aside)]
    A --> DB[(Primary DB)]
    DB --> R[(Read replicas)]
    CA --> R
```

## 2. Write path with async fanout (feeds, notifications, timelines)

```mermaid
flowchart LR
    C[Client] --> API[Write API]
    API --> DB[(Primary store)]
    API --> Q[[Message queue]]
    Q --> W1[Worker - fanout]
    Q --> W2[Worker - analytics]
    W1 --> T[(Timeline / index\nper-follower)]
    C -. eventual .-> T
```

Trade-offs: queue adds delay + at-least-once duplicates (idempotency); fanout-on-write costs storage, fanout-on-read costs read latency.

## 3. Master–slave replication + failover

```mermaid
flowchart LR
    LB[Load balancer] --> M[(Master\nR/W)]
    M --> S1[(Slave - read)]
    M --> S2[(Slave - read)]
    HB{{heartbeat}} -.-> P[(Promoted\nslave)]
    S2 -.failover.-> P
```

Trade-offs: read scale + HA vs replication lag, promotion logic, unreplicated-write loss window.

## 4. Sharding (consistent hashing)

```mermaid
flowchart LR
    R[Router / hash ring] --> H1[(Shard 0-1)]
    R --> H2[(Shard 1-2)]
    R --> H3[(Shard 2-3)]
    H1 -. replicate .-> H1R[(Replica)]
```

Trade-offs: horizontal growth vs cross-shard joins, hot-shard skew, rebalancing (consistent hashing minimizes moves).

## 5. Federation (functional partitioning)

```mermaid
flowchart LR
    A[App] --> D1[(Users DB)]
    A --> D2[(Orders DB)]
    A --> D3[(Posts DB)]
```

Trade-offs: less traffic per DB + cache locality vs app-level routing and painful cross-DB joins.

## 6. Job pipeline with back pressure

```mermaid
flowchart LR
    C[Client] --> API[API]
    API -->|queue full: 503 + backoff| Q[[Bounded queue]]
    Q --> W[Workers - autoscaled]
    W --> DB[(Result store)]
```

## 7. Active–passive vs active–active edge

```mermaid
flowchart LR
    subgraph AP [Active-passive]
      LB1[LB] --> A1[Active]
      A1 -.heartbeat.-> S1[Standby]
    end
    subgraph AA [Active-active]
      LB2[LB] --> B1[Active]
      LB2 --> B2[Active]
    end
```

## 8. Multi-region read path (CDN + geo DNS)

```mermaid
flowchart LR
    U1[User - NA] --> DNS[Geo/latency DNS]
    U2[User - EU] --> DNS
    DNS --> R1[Region NA - origin]
    DNS --> R2[Region EU - origin]
    R1 <-->|async replication| R2
    U1 -. hit .-> CDN1[(CDN edge)]
    U2 -. hit .-> CDN2[(CDN edge)]
```

## Conventions

- Solid arrow = synchronous request path; dashed = async/replication/eventual.
- Double parentheses `[( )]` = data store; `[[ ]]` = queue.
- Always show the LB (or note internal LBs elided) and mark stateless app tier.
- Annotate the consistency choice on cross-node arrows (sync vs async).
