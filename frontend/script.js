/**
 * script.js
 * ---------
 * Handles switching views, calling the search API, and rendering results.
 *
 * NOTE: Because the frontend and backend are deployed together on
 * the SAME Vercel domain, we use a relative path ("") instead of a
 * full URL.
 */

const API_BASE_URL = ""; // same-domain deployment — leave this empty

const centerWrapper = document.getElementById("centerWrapper");
const resultsPage = document.getElementById("resultsPage");
const resultsContainer = document.getElementById("resultsContainer");
const resultsMeta = document.getElementById("resultsMeta");

const searchInput = document.getElementById("searchInput");
const searchInputTop = document.getElementById("searchInputTop");
const searchButton = document.getElementById("searchButton");

async function performSearch(query) {
  query = query.trim();
  if (!query) return;

  centerWrapper.style.display = "none";
  resultsPage.style.display = "block";
  searchInputTop.value = query;

  resultsMeta.textContent = "Searching...";
  resultsContainer.innerHTML = `<div class="loading">Loading results...</div>`;

  try {
    const url = `${API_BASE_URL}/api/search?q=${encodeURIComponent(query)}`;
    const response = await fetch(url);

    if (!response.ok) {
      throw new Error(`Server responded with status ${response.status}`);
    }

    const data = await response.json();
    renderResults(data);

  } catch (err) {
    console.error("Search failed:", err);
    resultsMeta.textContent = "";
    resultsContainer.innerHTML = `
      <div class="error-msg">
        ⚠️ Couldn't reach the search backend. (${err.message})
      </div>`;
  }
}

function renderResults(data) {
  resultsMeta.textContent = `${data.count} result${data.count === 1 ? "" : "s"} for "${data.query}"`;

  if (!data.results || data.results.length === 0) {
    resultsContainer.innerHTML = `<div class="no-results">No results found. Try a different search term.</div>`;
    return;
  }

  resultsContainer.innerHTML = data.results.map(buildResultCardHTML).join("");
}

function buildResultCardHTML(result) {
  const escape = (str) =>
    String(str).replace(/[&<>"']/g, (c) => ({
      "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;"
    }[c]));

  return `
    <div class="result-item">
      <div class="result-url">${escape(result.url)}</div>
      <a class="result-title" href="${escape(result.url)}" target="_blank" rel="noopener noreferrer">
        ${escape(result.title)}
      </a>
      <div class="result-snippet">${escape(result.snippet)}...</div>
      <div class="result-score">relevance score: ${result.score}</div>
    </div>
  `;
}

searchButton.addEventListener("click", () => performSearch(searchInput.value));

searchInput.addEventListener("keydown", (e) => {
  if (e.key === "Enter") performSearch(searchInput.value);
});

searchInputTop.addEventListener("keydown", (e) => {
  if (e.key === "Enter") performSearch(searchInputTop.value);
});
