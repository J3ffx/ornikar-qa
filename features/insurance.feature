Feature: Testing the website UI
  Scenario: Verify main CTA functionality
    Given the user is on the landing page
    When the user clicks main cta
    Then the user should be redirected to the subscription page

  Scenario: Verify secondary CTA functionality
    Given the user is on the landing page with a pending estimation
    When the user clicks secondary cta
    Then the user should catch up the estimation

  Scenario: Verify scrolling to "Rubrique des guides"
    Given the user is on the landing page
    When the user scrolls down to see "Rubrique des guides"
    Then the user should see "Rubrique des guides" on the page