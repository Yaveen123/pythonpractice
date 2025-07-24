



```sql
SELECT A.Name, B.Name 
FROM Products A
INNER JOIN Suppliers B
ON A.SupplierID = B.SupplierID
WHERE A.Mass > 50, A.Producer = 'Yumtreats' 
ORDER BY DESC;
```