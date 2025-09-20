# Reflection: The Impact of AI on My Build Process

## Introduction

Integrating AI into my build process for the Polly-API project has been a transformative experience. Leveraging tools like GitHub Copilot and conversational AI assistants, I was able to accelerate development, improve code quality, and learn new best practices. This reflection explores what worked well, the limitations I encountered, and the lessons learned about prompting, reviewing, and iterating with AI.

## What Worked Well

One of the most significant benefits of using AI was the speed at which I could generate boilerplate code and API client functions. For example, when I needed a function to register a user or fetch paginated poll data, the AI provided accurate, ready-to-use code snippets that matched my OpenAPI specification. This allowed me to focus more on the business logic and less on repetitive coding tasks. The AI also helped with documentation, error handling, and even provided suggestions for best practices, such as using `response.raise_for_status()` for HTTP error handling and including authentication headers for protected endpoints.

Another area where AI excelled was in code review and troubleshooting. When I encountered errors, such as duplicate function definitions or incorrect function calls, the AI quickly identified the issues and suggested precise fixes. This iterative feedback loop reduced debugging time and increased my confidence in the codebase. The AI's ability to explain code in detail also deepened my understanding of the underlying logic, making it easier to maintain and extend the project.

## What Felt Limiting

Despite these advantages, there were some limitations. The AI occasionally struggled with context, especially when the project structure was complex or when files outside the workspace were involved. For example, it could not access or modify configuration files outside the allowed directory, which required manual intervention. Additionally, while the AI-generated code was generally correct, it sometimes missed subtle details, such as specific error handling for different HTTP status codes or the need for more granular logging. This meant that I still needed to carefully review and test the code before deploying it.

Another limitation was the AI's reliance on clear and specific prompts. Vague or ambiguous instructions often led to incomplete or incorrect code. This required me to refine my prompting skills, providing detailed context and explicit requirements to get the best results. The AI also occasionally repeated code or left behind orphaned fragments, which needed manual cleanup.

## Lessons Learned: Prompting, Reviewing, and Iterating

Working with AI taught me the importance of clear communication. The quality of the AI's output was directly related to the clarity and specificity of my prompts. I learned to break down complex tasks into smaller, actionable steps and to provide as much relevant context as possible. Reviewing the AI-generated code was essential; I could not assume correctness without verification. Iterating on the code—by refining prompts, testing, and incorporating feedback—led to better outcomes and a more robust codebase.

## Conclusion

Overall, AI had a profoundly positive impact on my build process. It accelerated development, improved code quality, and served as a valuable learning tool. However, it also highlighted the need for human oversight, clear communication, and iterative refinement. By combining the strengths of AI with careful review and thoughtful prompting, I was able to build a more effective and maintainable API project.
