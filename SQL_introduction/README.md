# SQL - Introduction

![image](https://github.com/Tunzale1/holbertonschool-higher_level_programming/assets/114104944/0f809f16-8d51-4a12-af91-61d0e8c863c4)
## What are databases?
Storing data in your application (in memory) has the obvious shortcoming that, whatever the technology you’re using, your data dies when your server stops. Some programming languages and/or frameworks take it even further by being stateless, which, in the case of an HTTP server, means your data dies at the end of an HTTP request. Whether the technology you’re using is stateless or stateful, you will need to persist your data somewhere. That’s what databases are for.

A solid database is expected to be **acid**, which means it guarantees:
- **A**tomicity: transactions are atomic, which means if a transaction fails, the result will be like it never happened.
- **C**onsistency: you can define rules for your data, and expect that the data abides by the rules, or else the transaction fails.
- **I**solation: run two operations at the same time, and you can expect that the result is as though they were ran one after the other. That’s not the case with the JSON file storage you built: if 2 insert operations are done at the same time, the later one will fetch an outdated collection of users because the earlier one is not finished yet, and therefore overwrite the file without the change that the earlier operation made, totally ignoring that it ever happened.
- **D**urability: unplug your server at any time, boot it back up, and it didn’t lose any data.

You will definitely run into the concept of **“CRUD”** operations. It’s just a fancy way to refer to the 4 operations that can be performed on the data itself:
- **C**reate some data;
- **R**ead some data;
- **U**pdate some data;
- **D**estroy some data.

## 2+ kinds of databases
When people talk about databases, they’re usually referring to relational databases (such as PostgreSQL, MySQL, Oracle, …); but there are many other kinds of databases used in the industry, which are globally referred to as “NoSQL” databases, even though they can be very different from each other, and serve very various purposes. Also, the name “NoSQL” comes from SQL, which is the name of the syntax used to give orders (CRUD operations, creating and deleting tables, …) to a relational databases; however, some non-relational databases, which are referred to as “NoSQL” give the option to use the SQL syntax.

## SQL
In order to work with relational databases, you will need to get familiar with SQL syntax. A lot of developers will acknowledge that they find the SQL syntax unpleasantly hard to use, which has some outcomes:

- Engineers that are comfortable with SQL are very respected in the industry, even more so in this age where data has gotten so valuable. To be honest, the fact that I aced the SQL challenge on my Apple interview is probably a huge reason for me to have gotten the job; it turns out the initial role was a lot about manipulating data.
- The fear of SQL explains a lot why non-relational databases got called “NoSQL”, a bit like if it was a statement, a complain. Non-relational databases push a lot the button of not having to use SQL.
- Modern full-fledged frameworks contain tools that are called ORMs, and one of their roles is to abstract away SQL queries (which is good for day-to-day ease of use, but can turn out very dangerous). We’ll cover ORMs more later, but it’s worth noting that you do find back-end engineers in the industry who work with relational databases, but never write a line of SQL, which makes them a lot less valuable on a project.
- For a beginner, keep in mind that SQL’s syntax is a bit hard to wrap your head around, so maybe you should follow a tutorial first. Please don’t try to memorize the SQL syntax. I’ve used SQL extensively in very advanced cases, on systems with hundreds of millions of records, and I still go on Google each time I need to compose a SQL query.


