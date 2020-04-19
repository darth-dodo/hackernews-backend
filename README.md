# reimagined-broccoli

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
