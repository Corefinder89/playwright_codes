## Test Generator

Playwright comes with the ability to generate tests out of the box and is a 
great way to quickly get started with testing. It will open two windows, 
a browser window where you interact with the website you wish to test and 
the Playwright Inspector window where you can record your tests, copy the 
tests, clear your tests as well as change the language of your tests.

### Running Codegen

Use the `codegen` command to run the test generator followed by the URL of 
the website you want to generate tests for. The URL is optional, and you 
can always run the command without it and then add the URL directly into 
the browser window instead.

```
playwright codegen demo.playwright.dev/todomvc
```
#### Recording a test

Run codegen and perform actions in the browser. Playwright will generate 
the code for the user interactions. Codegen will look at the rendered page 
and figure out the recommended locator, prioritizing role, text and test 
id locators. If the generator identifies multiple elements matching the 
locator, it will improve the locator to make it resilient and uniquely 
identify the target element, therefore eliminating and reducing test(s) 
failing and flaking due to locators.

#### Generating locators

ou can generate locators with the test generator.

- Press the 'Record' button to stop the recording and the 'Pick Locator' 
button will appear.
- Click on the 'Pick Locator' button and then hover over elements in the 
browser window to see the locator highlighted underneath each element.
- To choose a locator click on the element you would like to locate and 
the code for that locator will appear in the field next to the Pick 
Locator button.
- You can then edit the locator in this field to fine tune it or use the 
copy button to copy it and paste it into your code.

#### Emulation

You can also generate tests using emulation to generate a test for 
a specific viewport, device, color scheme, as well as emulate the geolocation, 
language or timezone. The test generator can also generate a test while 
preserving authenticated state. for more information visit this 
[link](emulation.md)