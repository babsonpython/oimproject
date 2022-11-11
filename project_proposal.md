# Project Proposal

**Team Members: Cathy Liang & Wilson Xu**

## The Big Idea

The main idea of this project is to create a stock checker, which will help us check the Badminton Shuttlecocks stock. The checker will notify us through SMS when the product become in stock. The project will mainly explore three topics we learned this semester: Web Scraping, HTML, and API. The ultimate goal of this project is to apply in-class knowledge to real-life example, using python language to build functions to help us purchase a product that tends to run out of stock. 

## Learning Goal

Our shared goal for this project is to incorporate what we learned in this class into one project. We will learn how to use Web Scraping to track product availability, how to obtain specific data from the HTML and build functions for stock checker, how to get a text once the product is back in stock using Twilio API. In terms of individual goal, Cathy is really interested in seeing how programming could help us solve real-life issue. Wilson is interested in learning how python could help him solve the out-of-stock issue he has with Badminton Shuttlecocks. 

## Implementation Plan

**1. Getting the HTML**: We will probably use requests library, which will help us make web requests from the internet so that we could get the HTML for the website. 

**2. Check Product Stock**: Once we have the page HTML, we will use the information to help us understand whether the item is in stock or not. We could right click on the "out of stock" or "add to cart" button on the web page, and select "inspect" to look at where it is in the HTML. Then once we know what information we need from the HTML, we might use Beautiful Soup library for pulling data out of HTML file (parsing). Then, we build functions to help us check whether the product is in stock or not. 

**3. Notify through SMS**: The next phase of the project is to ensure we get a text once the item came back in stock. Twilio is an API that allows people to easily send text messages. Then we could write python code to help us get the notification on our phone if the product is in stock. 

## Project Schedule
- Week 1: Observing Web Scraping patterns
- Week 2: Building functions to check product stock as well as text messaging
- Week 3:  Improving functionality of code
- Week 4-Week 8: Finalizing the project and building project website

## Collaboration Plan

We will pair program the entire project: learn the pattern together as well as developing a plan to reach our ultimate goal. The task will be divided into small part and splited evenly. 

## Risks

The website has anti-web scraping techniques that prevent us from getting the data. Or the website change its web design (html). Also, we need to keep the server running the entire time. 

## Additional Course Content

Most content and similar case could be found online. 