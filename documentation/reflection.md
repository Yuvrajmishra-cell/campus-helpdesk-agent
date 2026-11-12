# Part F – Project Reflection

Working on this project helped me understand how different AI-agent technologies work together. Before starting, I had very little knowledge of Skills, Plugins, MCP servers, or Git worktrees. Building the Campus Helpdesk Agent gave me practical experience with each of these concepts.

A **Skill** provides an AI assistant with instructions and knowledge for performing a particular task. In this project, the `timetable-helper` Skill explains how to answer student timetable questions using a CSV file. A **Plugin** packages related features together, such as Skills, custom commands, hooks, and MCP configuration. It makes these features easier to organize and distribute.

An **MCP server** provides a standard way for an AI application to access external tools and resources. My Python MCP server provides two tools: checking a batch timetable and checking a student's fee status. It also provides a hostel rules resource. I tested these features using MCP Inspector.

**Git worktrees** allow multiple branches of the same Git repository to be checked out in separate working directories. I created separate branches for Skill testing, MCP server development, and hook fixes. When two branches modified the same file, Git reported a merge conflict. I compared both versions, resolved the conflicting changes, and completed the merge.

I would choose a **Skill** when the main requirement is to give an AI assistant reusable instructions and task-specific knowledge. I would choose **MCP** when the assistant needs to interact with external systems, data, tools, or resources through a standard interface. They can also work together: a Skill can explain when and how an assistant should use an MCP tool.

I learned that AI should not be trusted with every decision without human review. I would never blindly delegate destructive terminal commands, security permissions, handling of private information, database deletion, production deployment, or Git merges without checking the consequences. AI-generated commands, package names, documentation links, and technical claims should also be verified.

Overall, this assignment taught me that AI is a useful development assistant, but human understanding, testing, and responsibility are still necessary for building reliable and secure systems.