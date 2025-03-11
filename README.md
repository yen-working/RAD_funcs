# RAD_funcs
### Description
Repo with misc. functions useful for Imaging Core. Include scripts to interact with Database, REDCap and Inteleshare.

### Content
Each script is a notebook with documentations. Suggested documentation template:

```
# Problem Statement
[This is where you explain the problem at hand. What is the usage for this script?]

# Solution
[A very brief summary of what the notebook does to solve the problem. Keep to 1-2 paragraphs max.]

A warning should be formatted as a H3 heading:
### This is an example warning.

# Instructions
[Instructions if needed.]

# Code 
[Where code blocks go.]
```

### Notes
1. REDCap:

- **Always** test in a Test project before running any scripts on the Target project. Refer to `REDCap/copy_records_redcap.ipynb` on how to mirror the Target project in the Test project.
- Whenever exporting data from REDCap, use argument `export_blank_for_gray_form_status=True` to differentiate between forms that are incomplete vs. forms that are unfilled. Without setting this argument, these two are indistinguishable.

### Enhancement lists
- Script to spin up local Docker instance and run DAGs.

