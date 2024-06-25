# lion-chat Dashboard

## Overview

The LionAGI Dashboard is a modern interface for managing AI models, agents, and data sources. It offers a streamlined way to configure and interact with various AI tools, including language models, data sources, and orchestrators.

## Features

- **LLM Configuration**: Choose and configure large language models (LLMs) like GPT-3, GPT-4, and Claude.
- **API Data Sources**: Manage API data sources, add new sources, and view existing ones.
- **Agent Management**: Create and manage agents with specific capabilities.
- **Orchestrator Controls**: Interact with the LionAGI orchestrator for advanced AI operations.
- **Data Sources**: Manage database connections, local files, and other data sources.

## Pages

### 1. LLM Configuration

![LLM Configuration](path/to/image1.png)

Configure LLM settings by selecting the model, setting the temperature, and specifying the maximum tokens.

### 2. API Data Sources

![API Data Sources](path/to/image2.png)

Add new API data sources by providing the API name, URL, key, and type. View and manage existing API sources.

### 3. Agent Management

![Agent Management](path/to/image3.png)

Create and manage agents by specifying their name, description, and capabilities. View existing agents and their details.

### 4. Orchestrator Controls

![Orchestrator Controls](path/to/image4.png)

Interact with the LionAGI orchestrator by providing instructions, context, and selecting tools. Manage orchestrator settings and view chat interactions.

### 5. Data Sources

![Data Sources](path/to/image5.png)

Manage various data sources, including databases and local files. Add new database connections by specifying the database name, type, connection string, username, and password.

## Getting Started

### Prerequisites

- Python 3.10 or higher
- Streamlit
- Streamlit Elements

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/lionagi-dashboard.git
   cd lionagi-dashboard
   ```

2. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

To run the application, use:

```bash
streamlit run app.py
```

## Customization

### Global Styles

Customize the global styles in the `set_global_styles` function within `app.py`. Modify the CSS variables to change the color scheme and styling.

### Adding New Features

To add new features or pages, create a new function in the appropriate module (e.g., `tabs`, `data_sources`, `agent_utils`) and update the main content area to include the new functionality.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue to discuss your ideas.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Replace the placeholder image paths with the actual paths to the images in your repository.