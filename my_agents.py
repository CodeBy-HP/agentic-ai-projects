from agents import Agent
from config import Config
from prompts import SalesAgentPrompts, EmailFormatterPrompts, ManagerPrompts
from tools import send_html_email


def create_sales_draft_agents() -> tuple[Agent, Agent, Agent]:
    """
    Create the three sales draft generation agents with different writing styles.

    Returns:
        Tuple of (professional_agent, engaging_agent, concise_agent)
    """
    professional_agent = Agent(
        name="Professional Sales Agent",
        instructions=SalesAgentPrompts.PROFESSIONAL_SALES_AGENT,
        model=Config.AZURE_MODEL,
    )

    engaging_agent = Agent(
        name="Engaging Sales Agent",
        instructions=SalesAgentPrompts.ENGAGING_SALES_AGENT,
        model=Config.AZURE_MODEL,
    )

    concise_agent = Agent(
        name="Concise Sales Agent",
        instructions=SalesAgentPrompts.CONCISE_SALES_AGENT,
        model=Config.AZURE_MODEL,
    )

    return professional_agent, engaging_agent, concise_agent


def create_email_formatting_agents() -> tuple[Agent, Agent]:
    """
    Create agents responsible for email subject writing and HTML conversion.

    Returns:
        Tuple of (subject_writer_agent, html_converter_agent)
    """
    subject_writer_agent = Agent(
        name="Email Subject Writer",
        instructions=EmailFormatterPrompts.SUBJECT_WRITER,
        model=Config.AZURE_MODEL,
    )

    html_converter_agent = Agent(
        name="HTML Email Body Converter",
        instructions=EmailFormatterPrompts.HTML_CONVERTER,
        model=Config.AZURE_MODEL,
    )

    return subject_writer_agent, html_converter_agent


def create_agent_tools(
    professional_agent: Agent,
    engaging_agent: Agent,
    concise_agent: Agent,
    subject_writer_agent: Agent,
    html_converter_agent: Agent,
) -> tuple[list, list]:
    """
    Create tools from agents for use by manager agents.

    Args:
        professional_agent: The professional sales agent
        engaging_agent: The engaging sales agent
        concise_agent: The concise sales agent
        subject_writer_agent: The subject writer agent
        html_converter_agent: The HTML converter agent

    Returns:
        Tuple of (sales_manager_tools, email_manager_tools)
    """
    # Tools for sales manager to call different draft generators
    professional_tool = professional_agent.as_tool(
        tool_name="professional_agent",
        tool_description="Generate a professional, serious sales email draft.",
    )

    engaging_tool = engaging_agent.as_tool(
        tool_name="engaging_agent",
        tool_description="Generate a witty, humorous sales email draft.",
    )

    concise_tool = concise_agent.as_tool(
        tool_name="concise_agent",
        tool_description="Generate a short, concise sales email draft.",
    )

    sales_manager_tools = [professional_tool, engaging_tool, concise_tool]

    # Tools for email manager to format and send emails
    subject_tool = subject_writer_agent.as_tool(
        tool_name="subject_writer",
        tool_description="Write a subject for a cold sales email",
    )

    html_tool = html_converter_agent.as_tool(
        tool_name="html_converter",
        tool_description="Convert a text email body to an HTML email body",
    )

    email_manager_tools = [subject_tool, html_tool, send_html_email]

    return sales_manager_tools, email_manager_tools


def create_manager_agents(
    sales_manager_tools: list, email_manager_tools: list
) -> tuple[Agent, Agent]:
    """
    Create the manager agents that orchestrate the workflow.

    Args:
        sales_manager_tools: Tools for the sales manager
        email_manager_tools: Tools for the email manager

    Returns:
        Tuple of (sales_manager, email_manager)
    """
    email_manager = Agent(
        name="Email Manager",
        instructions=ManagerPrompts.EMAIL_MANAGER,
        tools=email_manager_tools,
        model=Config.AZURE_MODEL,
        handoff_description="Convert an email to HTML and send it",
    )

    sales_manager = Agent(
        name="Sales Manager",
        instructions=ManagerPrompts.SALES_MANAGER,
        tools=sales_manager_tools,
        handoffs=[email_manager],
        model=Config.AZURE_MODEL,
    )

    return sales_manager, email_manager


def setup_all_agents() -> Agent:
    """
    Set up and configure all agents in the system.

    Returns:
        The sales_manager agent (entry point for the system)
    """
    # Create all individual agents
    professional_agent, engaging_agent, concise_agent = create_sales_draft_agents()
    subject_writer_agent, html_converter_agent = create_email_formatting_agents()

    # Create tools from agents
    sales_manager_tools, email_manager_tools = create_agent_tools(
        professional_agent,
        engaging_agent,
        concise_agent,
        subject_writer_agent,
        html_converter_agent,
    )

    # Create and return manager agents
    sales_manager, email_manager = create_manager_agents(
        sales_manager_tools, email_manager_tools
    )

    return sales_manager
