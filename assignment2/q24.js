// Q24. Use try-catch to handle a SyntaxError when parsing an invalid JSON string.

let jsonString = '{"name": John" "age": "30"}';

try {
  let obj = JSON.parse(jsonString);
  console.log("Parsed object:", obj);
} catch (error) {
  if (error instanceof SyntaxError) {
    console.log("Invalid JSON format");
    console.log("Error details:", error.message);
  } else {
    console.log("Error:", error.message);
  }
}
