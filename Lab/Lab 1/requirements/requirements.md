# Requirements Table

Second-Hand Product Escrow Marketplace

| ID | Type | Description | Priority | Acceptance Criteria | Rationale |
| --- | --- | --- | --- | --- | --- |
| FR-001 | Functional | Allow a seller to publish a used product with price, condition and photos, and a buyer to place an order against an available listing. | High | A complete listing becomes visible. A confirmed order reserves it and a competing order is rejected. | Makes offers discoverable and prevents double sales. |
| FR-002 | Functional | On confirmed payment, lock the full amount in escrow and move the order to Under Inspection. | High | A successful payment creates one hold for the order. Failed or repeated payments create no duplicate hold or payout. | Protects buyer funds before verification. |
| FR-003 | Functional | Allow only the assigned independent inspection agent to submit a signed condition report with a verifiable outcome. | High | An approved report moves the funded order to Awaiting Buyer Sign-off. A failed report leaves funds held and prevents release. | Provides independent condition evidence. |
| FR-004 | Functional | Allow the authenticated buyer to sign off and release funds once when a successful inspection exists and no dispute is active. | High | Both approvals and no active dispute produce one seller payout. Missing approval or an active dispute blocks payout, including on retry. | Enforces dual approval. |
| FR-005 | Functional | Allow the buyer to open a dispute before release and a dispute officer to resolve it with a recorded reason. | High | Opening a dispute freezes the hold. A rejection decision refunds the buyer. A dismissal restores the prior workflow and retains both approval requirements. | Provides a review trail and a path to refund. |
| NFR-001 | Non-functional (security and performance) | Freeze escrow when a dispute is acknowledged and prevent withdrawal of disputed funds throughout investigation. | High | With 100 concurrent simulated requests, 95% of valid dispute submissions acknowledge within one second. In release/withdrawal races, no disputed funds move after the freeze commits. | Prevents loss during review and sets a measurable response target. |
| NFR-002 | Non-functional (reliability) | Maintain consistent order and escrow records across retries and interrupted processing. | High | After duplicate payment notifications and a simulated restart, one hold exists per order, at most one payout or refund exists, and ledger totals reconcile. | Prevents duplicate settlement and supports recovery. |
