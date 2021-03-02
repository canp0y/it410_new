# Domain Driven Design

This is a paper stock trading system, providing users a potential platform to trade paper stocks. Among users, there's a ranking list, and users with more money will rank higher.
There will be four parts in the DDD document:
1. [Domain Events](#Domain-Events)
2. [Domain Commands](#Domain-Commands)
3. [Entities](#Entities)
4. [Value objects](#Value-Objects)

## Domain Events

#### Account Events
    1. Account Created 
    2. Password Changed
### Session Events
    1. Session Created
    2. Session Deleted
### Client Events
    1. Market Data Created
    2. Market Data Updated
    3. Portfolio Updated
    4. Portfolio Validated
### Transaction Events
    1. Transaction Record created
    2. Transaction Record Updated
### Ranking Events
    1. Ranking List created
    2. Ranking List Updated
    3. Ranking List Removed
---
## Domain Commands
#### Account Commands
    * Register an account
    * Validate account
    * Change Password
#### Client Commands
    * Call Stock API
    * Update Market
    * Create a transaction (Submit a Transaction)
    * Validate remainning cash
    * Update Portfolio
#### Ranking Commands
    * Create a list
    * Load users
    * Validate Portfolio
    * Rank User based on portfolio
    * Update ranking list
---
## Entities
### User Entities
<table>
  <thead>
    <tr>
      <th>Property</th>
      <th>Type</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>user_id</td>
      <td>UUID int(5)</td>
      <td>The user ID is auto-generated, assigned, and random-assigned. This is used for identify users.</td>
    </tr>
    <tr>
      <td>username</td>
      <td>char(40)</td>
      <td>Display name for users</td>
    </tr>
    <tr>
      <td>password</td>
      <td>Algorithm encrypted char(256)</td>
      <td>Users's password</td>
    </tr>
  </tbody>
</table>

### Market Entities
<table>
  <thead>
    <tr>
      <th>Property</th>
      <th>Type</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>stock_id</td>
      <td>int(5)</td>
      <td>The stock ID is auto-generated, assigned, and random-assigned. This is used for identify stock.</td>
    </tr>
    <tr>
      <td>ticker</td>
      <td>char(40)</td>
      <td>Tickers for stocks</td>
    </tr>
    <tr>
      <td>description</td>
      <td>text(400)</td>
      <td>Description for this stock</td>
    </tr>
    <tr>
      <td>mktvalue</td>
      <td>float</td>
      <td>Total Market Value for this stock</td>
    </tr>
    <tr>
      <td>avgPrice</td>
      <td>float</td>
      <td>Average Price for this stock</td>
    </tr>
    <tr>
      <td>vali_date</td>
      <td>datetime</td>
      <td>Valid datetime, default format "%y-%m-%d 00:00:00"</td>
    </tr>
  </tbody>
</table>

### Portfolio Entities
<table>
  <thead>
    <tr>
      <th>Property</th>
      <th>Type</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>position_id</td>
      <td>int(5)</td>
      <td>The position ID is auto-generated, assigned, and random-assigned. This is used for identify positions.</td>
    </tr>
    <tr>
      <td>user_id</td>
      <td>Foreign Key int(5)</td>
      <td>The user_id is imported from user table and is a foreign key.</td>
    </tr>
    <tr>
      <td>stock_id</td>
      <td>Foreign Key int(5)</td>
      <td>The stock_id is imported from market table and is a foreign key.</td>
    </tr>
    <tr>
      <td>number_of_shares</td>
      <td>float</td>
      <td>Number of shares</td>
    </tr>
    <tr>
      <td>bought_price</td>
      <td>float</td>
      <td>Price of shares when bought</td>
    </tr>
    <tr>
      <td>price</td>
      <td>float</td>
      <td>Current price of shares</td>
    </tr>
    <tr>
      <td>position_value</td>
      <td>float</td>
      <td>Total value of this stock</td>
    </tr>
  </tbody>
</table>

### Transaction Entities
<table>
  <thead>
    <tr>
      <th>Property</th>
      <th>Type</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>transaction_id</td>
      <td>int(5)</td>
      <td>The transaction ID is auto-generated, assigned, and random-assigned. This is used for identify transactions.</td>
    </tr>
    <tr>
      <td>user_id</td>
      <td>Foreign Key int(5)</td>
      <td>The user_id is imported from user table and is a foreign key.</td>
    </tr>
    <tr>
      <td>stock_id</td>
      <td>Foreign Key int(5)</td>
      <td>The stock_id is imported from market table and is a foreign key.</td>
    </tr>
    <tr>
      <td>stock_ticker</td>
      <td>char(40)</td>
      <td>Stock ticker</td>
    </tr>
    <tr>
      <td>type</td>
      <td>char(4)</td>
      <td>Either "Buy" or "Sell"</td>
    </tr>
    <tr>
      <td>price</td>
      <td>float</td>
      <td>The market price of stock</td>
    </tr>
    <tr>
      <td>num_of_shares</td>
      <td>float</td>
      <td>Number of shares included in this transaction</td>
    </tr>
    <tr>
      <td>total_price</td>
      <td>float</td>
      <td>Total Money in transaction</td>
    </tr>
  </tbody>
</table>

### User Money Entities
<table>
  <thead>
    <tr>
      <th>Property</th>
      <th>Type</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>user_id</td>
      <td>int(5)</td>
      <td>The user ID is imported from User Table and is a foreign key</td>
    </tr>
    <tr>
      <td>cash</td>
      <td>float</td>
      <td>Total Cash</td>
    </tr>
    <tr>
      <td>stock_value</td>
      <td>float</td>
      <td>Total value of all stocks</td>
    </tr>
    <tr>
      <td>total_money</td>
      <td>float</td>
      <td>Total money include cash and all stocks</td>
    </tr>
  </tbody>
</table>

---
## Value Objects
No Files will be used in this system.
