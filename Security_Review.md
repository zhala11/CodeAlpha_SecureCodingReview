# Secure Coding Review

## Project Overview

This project reviews a simple Python login application and identifies common security vulnerabilities.

## Language

Python

## Review Method

The code was reviewed using manual inspection with a focus on common application security issues.

## Findings

### 1. SQL Injection

**Severity:** High

**Vulnerable Code:**

The vulnerable application directly concatenates user input into an SQL query.

**Risk:**

An attacker may manipulate the SQL query and potentially bypass authentication or access unauthorized data.

**Remediation:**

Use parameterized SQL queries instead of string concatenation.

---

### 2. Plaintext Password Handling

**Severity:** High

**Vulnerable Code:**

The vulnerable application directly uses the entered password in the SQL query.

**Risk:**

Plaintext password handling can expose sensitive authentication information.

**Remediation:**

Passwords should be securely hashed and never stored or compared as plaintext.

---

### 3. Hardcoded / Unsafe Authentication Logic

**Severity:** Medium

**Risk:**

Weak authentication logic can make applications easier to attack.

**Remediation:**

Use secure authentication mechanisms, strong password policies, multi-factor authentication, and proper session management.

## Secure Coding Improvements

The secure version demonstrates:

* Parameterized SQL queries
* Password hashing
* Avoidance of SQL string concatenation
* Safer password input handling

## Conclusion

Manual code review identified several security weaknesses in the original application. The secure version applies safer coding practices to reduce the risk of SQL injection and insecure password handling.
