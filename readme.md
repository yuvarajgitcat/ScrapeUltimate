# ScrapeUltimate

## Project Overview
ScrapeUltimate is a universal web scraping application designed to extract structured data from diverse web pages. The tool supports multiple functionalities, including handling dynamic content, pagination, infinite scrolling, and attended mode for complex scenarios like captchas or login forms. This versatile scraper is powered by Selenium, Streamlit, and AI-based models, offering a comprehensive solution for web scraping needs.

---

## Features
- **Dynamic Content Handling**: Utilizes Selenium to scrape JavaScript-rendered websites.
- **Attended Mode**: Provides manual interaction for solving captchas or handling login forms.
- **Pagination Support**: Automatically navigates through paginated content.
- **Infinite Scroll Management**: Simulates scrolling to capture all dynamically loaded data.
- **AI Integration**: Employs models like OpenAI GPT and Llama for intelligent data extraction.
- **Output Flexibility**: Supports JSON, CSV, and Excel formats for downloaded data.
- **Cost Tracking**: Tracks token usage and associated AI processing costs.

---

## Methodology
The following image illustrates the methodology used in ScrapeUltimate:

![Methodology](https://github.com/yuvarajgitcat/ScrapeUltimate/blob/master/assets/methodology.png)

### Steps:

#### I. HTML Fetching and Preprocessing
1. Fetch raw HTML content using Selenium.
2. Simulate user interactions like scrolling to load dynamic content.
3. Clean the HTML by removing unnecessary elements (headers, footers).
4. Convert cleaned HTML into Markdown for easier parsing.

#### II. Input Website URL
- Supports single or multiple URLs for scraping.
- Batch processing for simultaneous data extraction.

#### III. Data Collection and Processing
1. Extract HTML content with Selenium for dynamic websites or BeautifulSoup for static ones.
2. Clean and preprocess data using BeautifulSoup.
3. Convert the content to Markdown using the `html2text` library.

#### IV. AI-Driven Data Extraction
- Process the data using AI models like OpenAI GPT or Llama.
- Generate dynamic schemas with Pydantic for structured extraction.

#### V. Local LLM Processing
- Use Llama 3.1 for advanced processing like summarization and classification.
- **Note**: Install [LLM Studio](https://lmstudio.ai) to route data to the local LLM for processing.

#### VI. Dynamic Data Models
- Create flexible schemas to match user-defined fields.
- Output structured data in JSON or Excel formats.

#### VII. Data Cleaning
- Refine raw data by removing noise and ensuring consistency.

#### VIII. Attended Mode
- Prompt manual intervention for captchas, logins, or other complex scenarios.

#### IX. Pagination and Infinite Scroll
- Handle multiple pages and dynamic scrolling to capture all data.

#### X. Additional Labels
- Improve transparency with contextual labels for specific steps.

#### XI. Data Storage and Output
- Organize results into unique folders for each session.
- Provide download options for JSON, CSV, or Excel formats.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yuvarajgitcat/scrapeultimate.git
