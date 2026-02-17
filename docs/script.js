// Demo handlers for the portfolio page.
const csvBeforeTable = document.getElementById("csv-before-table");
const csvAfterTable = document.getElementById("csv-after-table");
const scraperOutput = document.getElementById("scraper-output");
const emailOutput = document.getElementById("email-output");

const messyRows = [
  ["  Ava  ", " West ", "  420 "],
  ["  ", "East", "  0"],
  ["  Liam", " South ", "  155"],
];

const cleanedRows = [
  ["Ava", "West", "420"],
  ["Liam", "South", "155"],
];

const productRows = [
  "Wireless Mouse - $19.99",
  "USB-C Hub - $24.50",
  "Noise Cancelling Headphones - $89.00",
  "Laptop Stand - $32.25",
];

const emailTemplate = (name) =>
  `Hi ${name},\n\nThanks for signing up. Your setup guide is ready.\n\nCheers,\nAutomation Bot`;

function renderTable(table, rows) {
  if (!table) {
    return;
  }

  const tbody = table.querySelector("tbody");
  if (!tbody) {
    return;
  }

  tbody.innerHTML = rows
    .map(
      (row) =>
        `<tr>${row.map((cell) => `<td>${cell}</td>`).join("")}</tr>`
    )
    .join("");
}

function importCSV() {
  alert("Sample CSV imported successfully");
  renderTable(csvBeforeTable, messyRows);
}

function exportCSV() {
  alert("Cleaned CSV exported successfully");
  renderTable(csvAfterTable, cleanedRows);
}

function runScraper() {
  alert("Scraper demo executed");
  if (!scraperOutput) {
    return;
  }

  scraperOutput.innerHTML = productRows
    .map((product) => `<li>${product}</li>`)
    .join("");
}

function previewEmail() {
  alert("Email demo executed");
  if (!emailOutput) {
    return;
  }

  emailOutput.textContent = emailTemplate("Jordan");
}

// Expose handlers for inline button calls.
window.importCSV = importCSV;
window.exportCSV = exportCSV;
window.runScraper = runScraper;
window.previewEmail = previewEmail;
