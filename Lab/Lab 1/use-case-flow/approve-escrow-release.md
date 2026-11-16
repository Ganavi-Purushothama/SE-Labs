# UC-01 · Approve escrow release

## Preconditions

The buyer is signed in and owns the order. Full payment is held in escrow. The assigned inspection agent has certified the item and the order is Awaiting Buyer Sign-off.

## Postconditions

Success: one payout is recorded and the order closes as Completed. Alternate: escrow stays frozen, no payout is recorded, and the order is In Dispute.

## Main success scenario

1. The buyer opens the order and reviews the signed inspection report.
2. The buyer confirms acceptance of the inspected item.
3. The system verifies ownership, the inspection approval, the hold, and the absence of a dispute.
4. The system records buyer approval and authorizes one payout using the order identifier as the retry key.
5. After payout confirmation, the system records settlement, marks the order Completed, and shows the receipt.

## Alternate flow A1 · Buyer disputes condition

At step 2, the buyer selects Open Dispute and submits a reason. The system records the ticket and freezes the hold before acknowledging it. The order enters In Dispute and is routed to a dispute officer. The flow ends without a payout.
