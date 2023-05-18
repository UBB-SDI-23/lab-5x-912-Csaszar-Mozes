describe('Register + Login Test', () => {
  it('Tests Register Page', () => {
    let u_name = 'AlfaTest';
    let email = 'email@mail.test.com';
    cy.visit('http://localhost:4200/register')

    cy.contains('Username').type(u_name);
    cy.contains('E-mail').type(email);
    cy.contains('Password').type('A1aA1aA1a');
    cy.contains('Confirm password').type('A1aA1aA1a');

    cy.contains('Sign Up').click();
    cy.contains('Log In').click();

    cy.contains('Username').type(u_name);
    cy.contains('Password').type('A1aA1aA1a');
    cy.get('button:contains(Log In)').eq(1).click();

    cy.url().should('include', '/users/profile');
    cy.contains(/Logged in as/);
  })
})