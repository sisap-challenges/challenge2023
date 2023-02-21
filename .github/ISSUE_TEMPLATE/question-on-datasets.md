---
name: Question on datasets
about: Do you have a question about the dataset, subsets or projections? please ask here.
title: Question on datasets
labels: Question on datasets

body:
  - type: markdown
    attributes:
      value: |
        Do you have a question about the dataset, subsets or projections? please ask here.

  - type: input
    attributes:
      label: team
      description: Enter the name of your team
    validations:
      required: true

  - type: input
    attributes:
      label: task
      description: Enter the list of tasks of your interest
    validations:
      required: false

  - type: textarea
    attributes:
      label: question
      description: |
        Your question
    validations:
      required: true

---