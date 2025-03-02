import os
import pygit2
import re

library_github_repo = [
    'alainbonardi/abclib',
    'porres/pd-else',
    'porres/pd-cyclone',
    'wbrent/timbreIDLib',
]

for repo in library_github_repo:
    library_markdown = f'./docs/Libraries/{repo.split("/")[1]}.md'
    pattern_remove = r"^#X text -?\d+ -?\d+\s*"
    pattern_objcode = r"\b(\w+~)\b"
    repo_url = f'https://github.com/{repo}.git'
    repo_name = repo.split('/')[1]
    repo_path = f'./{repo_name}'

    if os.path.exists(repo_path):
        print(f'Updating {repo_name}')
        repo = pygit2.Repository(repo_path)
        remote = repo.remotes['origin']
        remote.fetch()
        repo.checkout('refs/remotes/origin/master')
    else:
        print(f'Cloning {repo_name}')
        pygit2.clone_repository(repo_url, repo_path)
    
    # loop recursively through all files in the repo
    objects_found = {}
    objects_names = []
    for root, dirs, files in os.walk(repo_path):
        for file in files:
            objname = file.replace('-help.pd', '')
            objects_names.append(objname)
            if file.endswith('-help.pd'):
                patch_filename = os.path.join(root, file)
                lines = []
                with open(patch_filename, 'r', encoding="ISO-8859-1") as patch_file:
                    lines = patch_file.readlines()

                text_files = []
                for line in lines:
                    length = len(line)
                    #print(length)
                    if line.startswith('#X text') and len(line) > 80:
                        text_files.append(line)
                objects_found[objname] = text_files
    
    with open(library_markdown, 'w') as library:
        library.write(f'# {repo_name}\n\n')
        for objname in sorted(objects_found.keys()):
            library.write(f'## `{objname}`\n\n')
            for line in objects_found[objname]:
                line = line.replace(' \\', '') 
                line = re.sub(pattern_remove, '', line)
                #for obj in objects_names:
                #    line = line.replace(obj, f'[{obj}](#{obj})')
                library.write(f'{line}\n')
            library.write('\n')
    