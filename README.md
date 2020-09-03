# Introduction
Its been a few years since I coded. However, I utilised a standard lib (_locale_) for currency conversion and localisation. I would always encourange the use of standard libs to solve common problems, however I would not recommend writing tests for them (no need to sharpen a knife twice).

I linked to two other projects which demostrate other skills I expect you want to see in this assessment. 

## Approach Taken
- Developer environment has been containerised for portability and testing 
    - Especially useful in a CI CD environement where we don't want to add every projects own unique build dependencies
    - Makes it easier for engineers to do the right thing and write tests
- Positive and Negative test cases given for demonstration purposes
- Utilised Parameterisation to make test cases easier to write
- I would advise the use of Property Bases Testing see [example demo](https://github.com/davidlpower/property_based_testing_demo) I gave while working as a *SEQ* in 2017


### What would I also like to add if I had time

Add Jenkins or CircleCI Pipeline which ran linting first and then the unit tests. I've added `set -e` to the `run.sh` file to emulate this (fails on first script error)

I have a seperate project [isOnline](https://github.com/davidlpower/isonline) which uses containerisation. I think it servers as another good example of how to containerise an application under test.

## CI Steps

- Linting ran as part of pipeline first to follow "_Fail Fast_" mindset
- Build Docker Image
- Run Tests
- Persist Image on Docker Image repository staging bucket
- Deploy Image and run Integration or E2E level tests
- Promote Image to prodction release candidate 
- Auto deploy to production
    - provided deployment has been observed as stable
    - downtime is minimal

# Scope

### In Scope

- Unit Tests

### Out of Scope

- Integration Tests
- Contract Tests
- E2E (Including UI) Tests


# Running The Code
To run this project's Linting and Tests please following these steps.
## Prerequisites
- Docker
## Run
- `./build_and_run_docker.sh`
