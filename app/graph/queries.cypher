// Phase 6/11 Neo4j prod — pure Cypher BFS/Dijkstra, no GDS
// Discovery: forward BFS to DEPOSIT_TO
MATCH p=(s:Wallet)-[:SENDS*1..5]->(d:DepositAddress)
WHERE s.address = $suspect
RETURN p LIMIT 25;
