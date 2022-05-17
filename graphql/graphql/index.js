const expressGraphQL = require('express-graphql');
const schema = require('./schema');

const graphql = expressGraphQL.graphqlHTTP({
  schema: schema,
  graphiql: true,
});

module.exports = graphql;
