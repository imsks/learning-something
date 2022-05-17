const {
  GraphQLSchema,
  GraphQLObjectType,
  GraphQLString,
  GraphQLList,
  GraphQLInt,
  GraphQLNonNull,
} = require('graphql');
// const BookType = require('./schema/book');
// const AuthorType = require('./schema/author');
const Models = require('./models');
const data = require('../data');

const RootQueryType = new GraphQLObjectType({
  name: 'Query',
  description: 'Root Query',
  fields: () => ({
    book: {
      type: Models.BookType,
      description: 'A single book',
      args: {
        id: { type: GraphQLInt },
      },
      resolve: (parent, args) => {
        return data.books.find((book) => book.id === args.id);
      },
    },
    books: {
      type: new GraphQLList(Models.BookType),
      description: 'List of books',
      resolve: () => books,
    },
    author: {
      type: Models.AuthorType,
      description: 'A single author',
      args: {
        id: { type: GraphQLInt },
      },
      resolve: (parent, args) => {
        return data.authors.find((author) => author.id === args.id);
      },
    },
    authors: {
      type: new GraphQLList(Models.AuthorType),
      description: 'An authors list',
      resolve: () => authors,
    },
  }),
});

const RootMutationType = new GraphQLObjectType({
  name: 'Mutation',
  description: 'Root Mutation',
  fields: () => ({
    addAuthor: {
      type: Models.AuthorType,
      description: 'Add an author',
      args: {
        name: { type: GraphQLNonNull(GraphQLString) },
      },
      resolve: (parent, args) => {
        const author = {
          id: data.authors.length + 1,
          name: args.name,
        };
        data.authors.push(author);
        return author;
      },
    },
    addBook: {
      type: Models.BookType,
      description: 'Add a book',
      args: {
        name: { type: GraphQLNonNull(GraphQLString) },
        authorId: { type: GraphQLNonNull(GraphQLInt) },
      },
      resolve: (parent, args) => {
        const book = {
          id: data.books.length + 1,
          name: args.name,
        };
        data.books.push(book);
        return book;
      },
    },
  }),
});

module.exports = new GraphQLSchema({
  query: RootQueryType,
  mutation: RootMutationType,
});
