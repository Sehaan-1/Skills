# OOD solutions — all 6 (distilled from `solutions/object_oriented_design/`)

Use for `ood` mode: classes/interfaces and relationships first, then methods. With the repo present: `.py` + `.ipynb` in each folder. Score with the OOD rubric in `rubric.md`.

## Shared method (from the notebooks)

1. Clarify constraints (generic vs specific? concurrency? persistence?) — each notebook opens with "Constraints and assumptions".
2. Nouns → classes; verbs → methods; identify inheritance vs composition.
3. Implement core operations; note invariants; sketch extensions (new card game, new vehicle size).

## 1. Hash map — `hash_table/`

```
Item(key, value)
HashTable(size)
  table: list[list[Item]]   # buckets → chaining
  _hash_function(key) = key % size
  set(key, value)   # update in bucket if key exists, else append
  get(key)          # scan bucket; KeyError if missing
  remove(key)       # delete from bucket
```

Talking points: collision resolution (chaining shown; open addressing alt), load factor / resize, integer-keys simplification vs generic hashable keys.

## 2. LRU cache — `lru_cache/` (same design as `query_cache` solution)

```
Node(results | query+results)
LinkedList: head/tail, move_to_front, append_to_front, remove_from_tail
Cache(MAX_SIZE)
  lookup: dict[key → Node]      # O(1) access
  linked_list                   # recency order
  get(q): hit → move_to_front; return results
  set(q, r): hit → update+move_to_front
             miss+full → pop lookup[tail], remove_from_tail
             miss+space → append_to_front, size++
```

Invariant: dict and list always updated **together**. Complexity: O(1) get/set. Talk: LFU/ARC alternatives, TTL vs pure LRU, why Redis `maxmemory-policy` matters.

## 3. Call center — `call_center/`

```
Rank = OPERATOR < SUPERVISOR < DIRECTOR   (Enum)
CallState = READY | IN_PROGRESS | COMPLETE
Call(rank, state, employee)
Employee(ABC): take_call, complete_call, escalate_call (abstract), _escalate_call → notify center
  ├─ Operator  escalates → call.level = SUPERVISOR
  ├─ Supervisor escalates → call.level = DIRECTOR
  └─ Director  cannot escalate (must handle any call)
CallCenter(operators, supervisors, directors)
  queued_calls: deque
  dispatch_call: pick rank's idle employee → else next-higher rank → else enqueue
  notify_call_escalated / notify_call_completed
```

Talking points: escalation chain as strategy per rank, queue when all busy, why Director.escalate raises NotImplementedError (LSP edge), concurrency on `employee.call is None`.

## 4. Deck of cards — `deck_of_cards/`

```
Suit = HEART | DIAMOND | CLUBS | SPADE
Card(ABC)(value, suit, is_available)
  BlackJackCard: is_ace (value==1), is_face_card (11–13 → score 10)
Hand(cards): add_card, score = sum(card.value)
  BlackJackHand: BLACKJACK=21; score() picks max score ≤ 21 else min bust
    possible_scores() — Aces counted 1 or 11
Deck(cards): deal_index, deal_card(), remaining_cards(), shuffle()
```

Talking points: abstract Card lets Poker/BlackJack subclass scoring; availability flag for dealt cards; ace duality drives `possible_scores`.

## 5. Parking lot — `parking_lot/`

```
VehicleSize = MOTORCYCLE | COMPACT | LARGE
Vehicle(ABC)(size, plate, spots_taken): can_fit_in_spot (abstract), take_spot, clear_spots
  Motorcycle: fits anywhere (spot_size 1)
  Car:        COMPACT or LARGE spot
  Bus:        5 consecutive LARGE spots
ParkingLot(num_levels) → levels[]: park_vehicle tries each level
Level(floor, total_spots): SPOTS_PER_ROW=10, available_spots,
  _find_available_spot, _park_starting_at_spot (contiguous span)
ParkingSpot(level, row, number, size): vehicle, is_available, can_fit_vehicle
```

Talking points: polymorphic `can_fit_in_spot` = open/closed extension for new vehicles; contiguous multi-spot allocation for buses; level→spot ownership both directions.

## 6. Online chat server — `online_chat/`

```
UserService: users_by_id; add/remove_user; friend request approve/reject
User: friends_by_id, friend_ids_to_private_chats, group_chats_by_id,
      received/sent_friend_requests_by_id
      message_user, message_group, send/receive/approve/reject_friend_request
Chat(ABC)(chat_id, users[], messages[])
  PrivateChat(first, second)
  GroupChat: add_user, remove_user
Message(message_id, message, timestamp)
AddRequest(from, to, RequestStatus, timestamp)
RequestStatus = UNREAD | READ | ACCEPTED | REJECTED
```

Talking points: relationship symmetry (store on both users?), request state machine, Chat abstraction covers 1:1 vs N:N, scaling notes (message feed fanout, presence via heartbeats — link the async/queues playbook).

## OOD ↔ system-design bridges

| OOD question | Scales into system design topic |
|---|---|
| LRU cache | Cache strategies, query_cache solution |
| Hash map | Key-value store abstraction |
| Chat server | WhatsApp design, message queues, websockets vs poll |
| Call center | Task queues / routing, availability |
| Deck of cards | API design, state machines |
| Parking lot | Allocation/sharding metaphors, resource pools |
