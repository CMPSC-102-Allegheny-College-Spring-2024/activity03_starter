## Survey

Approximation

## Assigned

Friday, 2 Feb 2024

## Due

Friday, 2 Feb 2024, 11:00am

## Project Goals

This assignment invites you to write, run and observe two Python functions; `fifth_root_approximation()` and `sixth_root_approximation()` that calculate the approximations of the fifth and six roots, respectively, of inputted values.

We note that both of these functions are very similar mathematically and in structure to the other root approximation functions that we already studied in class this week to approximate the second and third roots.

The objective of this activity is to determine the mathematical pattern and to implement a slight modification to complete the current code in `source/rootApproximation.py`.

This project offers you the opportunity to ensure that you understand how to (i) understand the basics of automated approximation and (ii) to recognize patterns to be used to evolve these root approximation calculators to find larger roots.

## Running your code

To run the source code, use the following command in your `source/` directory.

``` bash
python3 rootApproximation.py 
```

## Sample Output

With your working code, your output will be the following.

``` bash
Enter an integer to find the fifth root :550731776
guess = 220292710.4
guess = 176234168.32
...
guess = 56.00000000030222
guess = 56.0
The six root of 550731776
is approximately: 56.0
The floor of the value is : 56

Enter an integer to find the sixth root :128100283921
guess = 53375118300.416664
guess = 44479265250.34722
...
guess = 71.00000000109507
guess = 71.0
The six root of 128100283921
is approximately: 71.0
The floor of the value is : 71
```

## Writing

Once you have completed and tested your code, please go to the `writing/reflection.md` to dazzle your instructor with your brilliant reflections to several questions.

## Installations

If you have not yet installed Python, Poetry and GatorGrade, you may find instructions below about how to install this software.

- Install Python. Please see:
- [Setting Up Python on Windows](https://realpython.com/lessons/python-windows-setup/)
- [Python 3 Installation and Setup Guide](https://realpython.com/installing-python/)
- [How to Install Python 3 and Set Up a Local Programming Environment on Windows 10](https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-local-programming-environment-on-windows-10)
- Install `gatorgrade`
- First, [install `pipx`](https://pypa.github.io/pipx/installation/)
- Then, install `gatorgrade` with `pipx install gatorgrade`
- [Install `poetry`](https://python-poetry.org/docs/)
- Install `VSCode` or another editor. See [Getting Started with Python in VS Code](https://code.visualstudio.com/docs/python/python-tutorial)

## Cloning Your Repository

+ Use the link to the project that was given to you in class to _accept_ the assignment and find a link to your personalized project.
+ Once the importing task has completed, click on the created assignment link which will take you to your newly created GitHub repository for this lab.
+ Clone this repository (bearing your name) and work locally with out own installed editor and associated resources.
+ As you are working on your lab, you are to commit and push regularly. The commands are the following.

```
git add -A
git commit -m ``Your notes about commit here''
git push
```

After you have pushed your work to your repository, please visit the repository at the GitHub website (you may have to log-in using your browser) to verify that your files were correctly sent.

## Project Deliverables

Your assignment comprises the following:
+ Completing code in Python: `source/rootApproximation.py`
+ Writing in Markdown: `writing/reflection.md`

To help you write using Markdown, the following references may be helpful to you.
+ [Markdown Tidbits](https://www.youtube.com/watch?v=s-oSuHFVnR4)
+ [Markdown Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)

## Project Assessment

The grade that a student receives on this assignment will have the following components.

- **Mastery of Technical Writing [up to 75%]:**: Students will also receive a checkmark grade when the responses to the writing questions presented in the `reflection.md` reveal a proficiency of both writing skills and technical knowledge. To receive a check mark grade, the submitted writing should have correct spelling, grammar, and punctuation in addition to following the rules of Markdown and providing conceptually and technically accurate answers.

- **Mastery of Technical Knowledge and Skills [up to 25%]**: Students will receive a portion of their assignment grade when their program implementation reveals that they have mastered all of the technical knowledge and skills developed during the completion of this assignment. As a part of this grade, the instructor will assess aspects of the programming including, but not limited to, the completeness and the correctness of the program and the use of effective source code comments.

---

## GatorGrade Checking

You can also use `gatorgrade` to check the baseline requirements of this assignment by running the following command in your terminal:

`gatorgrade --config config/gatorgrade.yml`

If `gatorgrade` shows that all checks pass, you will know that you have met baseline requirements of this project.

## Check Your Submission
After you have pushed your work to your repository, please visit the repository at the GitHub website (you may have to log-in using your browser) to verify that your files were correctly sent.

## Project Assessment

This is a check mark grade.
