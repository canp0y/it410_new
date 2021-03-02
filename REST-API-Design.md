# REST API DESIGN
This REST API Design file is generated with the paper trading client. The purpose of this file specify different needs of the API.

### User (Entity)

| Properties       | Events | Commands | Quesies |
|---------|---|---|---|
| <ul><li>user_id (int)</li><li>user_name (string)</li></ul>| <ul><li>User created</li><li>User Updated</li><li>Password Changed</li><li>Transaction Record Created</li><li>Transaction Record Updated</li></ul>| <ul><li>Register an account</li><li>Validate Account</li><li>Change Password</li><li>Update Portfolio</li><li>Load Users</li></ul>|<ul><li>Get a list of users</li><li>Get a specific user</li><li>Post a trade</li></ul>|

### Stock (Entity)

| Properties       | Events | Commands | Quesies |
|---------|---|---|---|
| <ul><li>stock_id (int)</li><li>ticker (string)</li><li>description (string)</li><li>mktvalue (float)</li><li>avgPrice (Float)</li></ul>| <ul><li>Market Data created</li><li>Market Data Updated</li><li>Transaction Record Created</li><li>Transaction Record updated</li><li>Portfolio Record Created</li><li>Portfolio Record Updated</li></ul>| <ul><li>Call Stock API</li><li>Update Market</li><li>Create a Transaction</li></ul>|<ul><li>Get Stock Data</li><li>Post a trade</li></ul>|

### Wallet (Entity)

| Properties       | Events | Commands | Quesies |
|---------|---|---|---|
| <ul><li>user_id (int)</li><li>username (string)</li><li>cash (float)</li><li>stockValue (float)</li><li>totalMoney (Float)</li></ul>| <ul><li>Portfolio Created</li><li>Portfolio Updated</li></ul>| <ul><li>Create a transaction</li><li>Validate remainning cash</li></ul>|<ul><li>Get User Portfolio</li><li>Post a trade</li></ul>|

### Portfolio (Entity)

| Properties       | Events | Commands | Quesies |
|---------|---|---|---|
| <ul><li>user_id (int)</li><li>username (string)</li><li>positions (Array of Stock)</li></ul>| <ul><li>Portfolio Updated</li><li>Portfolio Validated</li><li>Transaction Record Created</li><li>Transaction Record updated</li><li>Ranking List Created</li><li>Ranking List Updated</li><li>Ranking List Removed</li></ul>| <ul><li>Validate Portfolio</li><li>Rank User based on Portfolio</li><li>Update Ranking List</li></ul>|<ul><li>Post A trade</li><li>Get User Ranking List</li></ul>|

## Define Endpoints
|Query|Url Fragment|HTTP Method| Path Parameters|
|-----------------|-------------|---------|--------|
|Get Stock Data|/stock|GET||
|Get All Users|/account/allUser|GET||
|Get A specific User|/account/allUser/{id}|GET|id|
|Get A User's Wallet|/wallet/{userName}|GET|userName|
|Get A User's Portfolio|/portfolio/{userName}|GET|userName|
|Submit a trade|/trade/{userName}|POST|userName|

## Representations

### User
```
"user": {
        "type": "object",
        "properties": {
          "user_id": {
            "type": "integer",
            "example": 10086
          },
          "username": {
            "type": "string",
            "example": "canp0y"
          }
        }
    }    
```

### Stock
```
 "stock": {
        "type": "object",
        "properties": {
          "stock_id": {
            "type": "string",
            "example": "10086"
          },
          "ticker": {
            "type": "string",
            "example": "AAPL"
          },
          "description": {
            "type": "string",
            "example": "APPLE Inc"
          },
          "mktvalue": {
            "type": "number",
            "example": 1800059740.56
          },
          "avgPrice": {
            "type": "number",
            "example": 146.23
          }
        }
      }
```

### Wallet
```
 "wallet": {
        "type": "object",
        "properties": {
          "userid": {
            "type": "integer",
            "example": 10086
          },
          "username": {
            "type": "string",
            "example": "Username"
          },
          "cash": {
            "type": "string",
            "example": "100$"
          },
          "stockValue": {
            "type": "string",
            "example": "5000$"
          },
          "taotalMoney": {
            "type": "string",
            "example": "5100$"
          }
        }
      }
```

## Field sets
* /stock?stockName=primary - Return a specific stock
* /stock?limit=int - Return a specific number of stocks (max:50)
* /account/allUser/?adminPass=primary - To return all users, it require adminPassword
* /account/allUser/?adminPass=primary&limit=int - Return a limited number of all users
* /account/allUser/{id}?adminPass=primary - Return a specific user with the adminPassword
* /wallet/{userName}?password=str - Users can check their wallet amount
* /portfolio/{userName}?password=str - Users can check their portfolio details
* /trade/{userName}?password=primary&ticker=primary&price=primary = User can post a transaction using these parameters

## HTTP Status Code
|Status Code| Meaning|Reference|
|-------|----------------------|-------------|
| 200 | The request was processed successfully. | |
| 400 | There is something wrong with the request. The response body would ideally include a description of what was wrong with the request. | [IETF rfc7231 Client Error 4xx](https://tools.ietf.org/html/rfc7231#section-6.5) [IETF rfc7231 400 Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1) |
| 401 | The request requires authentication and the request did not have authentication information. | [IETF rfc7235 401 Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1) |
| 403 | The request provided authentication information but the authenticated user is not authorized to get the results. | [IETF rfc7231 403 Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3) |
| 404 | This status code commonly indicates one of two things which may be distinguished using the response body. It could be that 1) the requested endpoint does not exist or 2) the requested resource does not exist. If the endpoint returns a collection then a `404` should not be used when the collection is empty, instead use a `200` and send back an empty array. | [IETF rfc7231 404 Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4) |

### Status Codes Meanings for Specific Methods

| Status Code | Method | Meaning | Reference |
| ----------- | ------ | ------- | --------- |
| 200 | GET | Resource or resources successfully retrieved. | |
| 201 | POST | The resource was created. If a response body is provided then it should represent the resource created. Additionally, a Location header should be set, specifying the endpoint for where the created resource can be retrieved. | [IETF rfc7231 POST](https://tools.ietf.org/html/rfc7231#section-4.3.3) |