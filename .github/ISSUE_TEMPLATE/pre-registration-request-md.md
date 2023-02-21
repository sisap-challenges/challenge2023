---
name: Pre-registration-request.md
about: Declares interest in participation in some of the Tasks of the SISAP23 challenge.
title: pre-registration info
labels: Pre-registration request
assignees: ''

---

body:
- type: markdown
  attributes:
    value: |
      **State the tasks of interest, listed in the [challenge site](https://sisap-challenges.github.io/tasks/)**

- type: input
  attributes:
    label: team
    description: >-
      Enter the name of your `team` wrapped with single backticks
  validations:
    required: true

- type: input
  attributes:
    label: corresponding
    description: >-
      Enter the username of your `corresponding` author wrapped with single backticks
  validations:
    required: true

- type: textarea
  attributes:
    label: subsets and projections
    description: |
      List the LAION subsets and projections that you plan to use
      - One combination per line,
      - Of course, you can change your mind, but this will help us to know what can be used as a first approach.
  validations:
    required: true      

- type: textarea
  attributes:
    label: members
    description: |
      Enter the initial members of your team
      - One member per line, affiliations
  validations:
    required: true

- type: checkboxes
  attributes:
    label: opensource
    description: |
      Are you willing to open source your solution?
    options:
    - label: Yes
      required: false

- type: checkboxes
  attributes:
    label: opensource
    description: |
      It is recommended to follow this repository to be informed of any changes and news.
    options:
    - label: Yes
      required: yes

...