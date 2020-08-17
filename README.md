# Introduction
I utilised a standard lib (_locale_) for currency conversion and localisation. I would always encourange the use of standard libs to solve common problems, however I would not recommend writing tests for them (no need to sharpen a knife twice).

## Approach Taken
- Positive and Negitive test cases given for demostration purposes
- Utilised Parameterisation to make test cases easier to write
- I would advise the use of Property Bases Testing see [example demo](https://github.com/davidlpower/property_based_testing_demo) I gave while working as a *SEQ* in 2017


### What would I also like to add if I had time

Containerise the application for improved developer portability. A Jenkins or CircleCI Pipeline would also be nice.

## CI Steps

- Linting ran as part of pipeline first to follow "_Fail Fast_" mindset
- Build Docker Image
- Run Tests
- Persist Image on Docker Image repository
- Deploy Image to Staging (in the case of staging)

# Scope

### In Scope

- Unit Tests

### Out of Scope

- Integration Tests
- Contract Tests
- E2E (Including UI) Tests
