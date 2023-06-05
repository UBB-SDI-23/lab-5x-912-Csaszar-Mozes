describe('template spec', () => {
  it('Checks Add Buttons Logged Out', () => {
    for (let url_part of ['companies', 'locations', 'pc', 'people']) {
      cy.visit('localhost:4200/' + url_part);
      cy.contains('Add').should('not.exist');
    }
  })

  it('Checks Add Buttons Logged In', () => {
    cy.visit('http://localhost:4200');
    cy.contains('Log In').click();
    let u_name = 'admin';

    cy.contains('Username').type(u_name);
    cy.contains('Password').type('Easy123Pass');



    cy.get('button:contains(Log In)').eq(1).click();

    cy.on('window:alert', (message) => {
      expect(message).to.equal('Login successful!');
    });
    cy.wait(1000);
    for (let url_part of ['companies', 'locations', 'pc', 'people']) {
      cy.visit('localhost:4200/' + url_part);
      cy.contains('ADD').should('exist');
    }
<<<<<<< HEAD

=======
>>>>>>> messaging
  })
})