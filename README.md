# reimagined-broccoli

## Product Features
- Listing of all the links (no login required)
- Link Creation
- User Creation
- JWT Based authentication
- Vote registration and unregistration by logged in Users

## Python env
- The project uses Python 3.7. Use [PyEnv](https://github.com/pyenv/pyenv) to install the required version
- Python environment in managed through [Poetry](https://python-poetry.org/)
- Install Poetry using instructions present [here]()
- Install the project virtual env and packages using the command. **Make sure you have set the `local` Python version to 3.7**
```sh
poetry install
```
- Start the project virtual env using the command
```
poetry shell
```
- To check out more details about your virtualenv please run the command
```sh
poetry env info
```
- In case of questions, please checkout the guide to maintaining virtual envs and python versions with over [here](https://python-poetry.org/docs/managing-environments/)

## Application Details
- Python 3.7
- Django 2.2
- Django Filters
- [Graphene Django](https://github.com/graphql-python/graphene-django)
- [Django GraphQL JWT](https://github.com/flavors/django-graphql-jwt)

## API interaction
- The GraphQL interface can be accessed using the inbuilt Graphene UI present at `localhost:8000/grapqhl` but it does not support JWT Auth
- To use GraphQL with JWT Auth checkout **[Insomnia](https://insomnia.rest/)** or **[Postman](https://www.postman.com/)**


# Precommit hooks
- isort
- flake8
- black
- in built precommit checks

## Application Details
- Django 2.2 application

## GraphQL
- The GraphQL interface can be accessed at `localhost:8000/graphql`
- GraphQL interfaces are of the following types:
    - Query - analogous to DQL statemets
    - Mutations - analogous to DML and DDL statements

---
### Query
- Fetch `Link`s data
```graphql
query {
  links {
    url
    description
    id
  }
}
```

- Fetch `HNUsers` data
```graphql
query{
  hnUsers{
    bio
    username
    email
    superuserAccess
  }
}
```

- Fetch JWT token user Details
```graphql
# provide the JWT in Auth headers

query{
  me {
    username
    email
  }
}
```

- Fetch List of Links with the HN User Information
```graphql
query {
  links{
    id
    url
    postedBy{
      username
    }
  }
}
```

---
### Mutations
- Create `Link`

```graphql
mutation {
  createLink(
  description: "Hustlers Den",
  url: "https://github.com/darth-dodo/hustlers-den"
  ){
    url
    description
    id
  }
}
```

```graphql
mutation {
  createLink(url: "https://github.com/darth-dodo/discuss-it", description: "Phoenix and Elixir clone") {
    id
    url
    description
    postedBy {
      username
      email
    }
  }
}
```

- Create HN User
```graphql
mutation {
  createHnUser(
    bio: "dummy bio"
    email: "dummy-user@email.com"
    password: "dummypassword"
    username: "dummy-1"
  ){
    hnUser {
      bio
    }
  }
}
```

```graphql
# generate the JWT payload

mutation {
  tokenAuth(username: "dummy-1", password: "dummypassword"){
    payload
  }
}
```

```graphql
# generate the JWT token

mutation {
  tokenAuth(username: "dummy-1", password: "dummypassword"){
    token
  }
}
```

```graphql
# verify the JWT token

mutation {
  verifyToken(token: "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImR1bW15LTEiLCJleHAiOjE1ODczMDg5NjksIm9yaWdJYXQiOjE1ODczMDg2Njl9.sBVGWqOnHxWv7f1zeJqb6V-CUZGZ4rxKDEIbqLtsZQY"){
    payload
  }
}
```


- Create Vote
```graphql
mutation {
  createVote(linkId: 4){
    vote {
      created
      user {
        username
      }
      link {
        url
      }
    }
  }
}
```

- Register Unvote
```graphql
mutation {
  registerUnvote(linkId: 4){
    success
  }
}
```
