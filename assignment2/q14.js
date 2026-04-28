// Q14. Display the reading status (book name, author name, and reading status) of books.

let library = [
  {
    author: "Bill Gates",
    title: "The Road Ahead",
    readingStatus: true,
  },
  {
    author: "Steve Jobs",
    title: "Walter Isaacson",
    readingStatus: true,
  },
  {
    author: "Suzanne Collins",
    title: "Mockingjay: The Final Book of The Hunger Games",
    readingStatus: false,
  },
];

library.forEach((book) => {
  console.log(
    `Title: ${book.title} | Author: ${book.author} | Read: ${book.readingStatus}`
  );
});
