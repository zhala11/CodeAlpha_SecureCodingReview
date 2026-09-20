# CodeAlpha Secure Coding Review

## Overview

This project was completed as part of the CodeAlpha Cyber Security Internship – Task 3.

The project demonstrates a security-focused code review of a Python login application. The original application was manually inspected to identify common security vulnerabilities and was then improved using secure coding practices.

## Application

**Programming Language:** Python

**Application:** Simple Login Application

## Review Method

The application was reviewed using manual code inspection with a focus on common security vulnerabilities.

## Security Issues Identified

* SQL Injection
* Insecure plaintext password handling
* Weak authentication logic

## Security Improvements

The secure version demonstrates:

* Parameterized SQL queries
* Password hashing
* Safer password input handling
* Avoidance of SQL query string concatenation

## Project Files

| File                 | Description                                              |
| -------------------- | -------------------------------------------------------- |
| `vulnerable_app.py`  | Original application containing security vulnerabilities |
| `secure_app.py`      | Improved version using secure coding practices           |
| `Security_Review.md` | Detailed findings and remediation recommendations        |

## Objective

The objective of this project is to demonstrate how manual secure coding reviews can identify vulnerabilities and how developers can apply security best practices to make applications safer.

## Internship

**Program:** CodeAlpha Cyber Security Internship
**Task:** Task 3 – Secure Coding Review
