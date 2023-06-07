function convertJsonToCsv(jsonData) {
    const separator = ",";
  
    // Extract column headers from the first object in the JSON
    const columns = Object.keys(jsonData[0]);
  
    // Build the CSV header
    const csvHeader = columns.join(separator);
  
    // Build the CSV rows
    const csvRows = jsonData.map((data) =>
      columns.map((column) => {
        let cell = data[column];
  
        // Convert numbers to strings, leaving other values unchanged
        if (typeof cell === "number") {
          return cell.toString();
        }
  
        // If the cell is not a string or contains a comma, wrap its content with double quotes
        if (typeof cell !== "string" || cell.includes(separator)) {
          return `"${cell}"`;
        }
  
        return cell;
      }).join(separator)
    );
  
    // Combine the header and rows into a single CSV string
    const csvContent = [csvHeader, ...csvRows].join("\n");
  
    return csvContent;
  }
  
  // Fetch JSON data from a URL
  fetch("https://example.com/api/data")
    .then((response) => response.json())
    .then((jsonData) => {
      // Convert JSON to CSV
      const csvData = convertJsonToCsv(jsonData);
      console.log(csvData);
  
      // Do further processing with the CSV data here
    })
    .catch((error) => {
      console.log("Error fetching JSON data:", error);
    });
  