// Q16. Parse a URL and return its components.

function parseURL(urlString) {
  try {
    const url = new URL(urlString);
    return {
      protocol: url.protocol,
      host: url.host,
      hostname: url.hostname,
      port: url.port,
      pathname: url.pathname,
      search: url.search,
      hash: url.hash,
      origin: url.origin,
      params: Object.fromEntries(url.searchParams),
    };
  } catch (error) {
    console.error("Invalid URL provided:", error.message);
    return null;
  }
}

const result = parseURL(
  "https://www.example.com:8080/path/page?name=John&age=30#section1"
);

console.log("Parsed URL:", result);
