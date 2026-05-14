# CYBERBLITZ 2026 Challenge Template

> [!IMPORTANT]  
> WIP
> Remove this note and update README when challenge is ready.

## Instructions for use

> [!NOTE]
> Need a reference to an actual example challenge? Check out [commit2main/cybltz2026-example-challenge](https://github.com/commit2main/cybltz2026-example-challenge).

1. Copy the repository via ["Use this template"](https://github.com/new?template_name=cybltz2026-chall-template&template_owner=cyberh4ts).
    - **Ensure your repository visibility is set to private!**
    - Update the repository name to match your challenge name
2. Update `README.md`.
    - Update the title ("CYBERBLITZ 2026 Challenge Template") to match your challenge name
    - Remove the "Instructions for use" section
    - Update the description, which will be used in the challenge listing
    - Update the author section with your name or email or handle or LinkedIn or whatever
3. Push your challenge files.
    - **Please use a standardised flag of `CYBLTZ2026{example_flag}` to prevent any leaks!** If you have a suggested flag, please let the EXCOs know privately so we can include it for the actual challenge release
    - [`distrib/`](distrib/) should contain the files you want to distribute to the participants (if applicable)
    - [`src/`](src/) should contain files required to host your challenge or to create the distributable files (if applicable)
        - e.g. Flask app, mp3 files, plaintext files, etc.
4. Update Docker configuration (if applicable). [Need a guide?](https://docker-curriculum.com/)
    - **You may delete the Docker files if your challenge does not require hosting**
    - Update [`Dockerfile`](src/Dockerfile) such that it is a complete image that can run your challenge
    - Update [`compose.yaml`](compose.yaml) to include any additional services required to host your challenge (e.g. database, etc.)
5. **Remember to test your challenge first**!
    - You can use `docker compose up` to test your hosted challenge locally
    - Ensure the files in `distrib/` are sufficient for participants to solve the challenge
6. **Add a writeup and solution files.**
    - This will be used for the official writeup release after the competition, so make sure it is complete and easy to understand!
    - Use the [`sol/`](sol/) directory to include your solution files.
    - Update [`sol/README.md`](sol/README.md) with the writeup and instructions to for the solution files (if applicable)
7. Once your challenge is ready, **add `@commit2main` (0x4973616163) as an admin collaborator** to your repository and inform the EXCOs.
    - You can add new collaborators from the "Settings" tab of your repository on Github, then "Collaborators and teams", then "Add people".

## Challenge Description

Category: [e.g. Pwn, Web, Crypto, Forensics, Misc, etc.]

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce dictum dolor nisl, vitae sodales magna dapibus vitae. Curabitur in facilisis turpis. Phasellus est nulla, hendrerit eu lobortis vel, pretium sit amet ex.

## Author

@johndoe
