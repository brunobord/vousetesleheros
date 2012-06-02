#!/usr/bin/env python
#-*- coding: utf-8 -*-
import os
import argparse
from codecs import open
import shutil
from jinja2 import Environment, FileSystemLoader
import yaml
import markdown

parser = argparse.ArgumentParser(u"Vous êtes le héros")
parser.add_argument('--root-dir', '-d', default=os.path.dirname(os.path.abspath(__file__)))
args = parser.parse_args()

ROOT_DIR = args.root_dir
STEP_DIR = os.path.join(ROOT_DIR, 'steps')
BUILD_DIR = os.path.join(ROOT_DIR, 'website')
ASSET_SOURCE_DIR = os.path.join(ROOT_DIR, 'assets')
ASSET_DEST_DIR = os.path.join(BUILD_DIR, 'assets')

for path in (STEP_DIR, BUILD_DIR, ASSET_DEST_DIR):
    if not os.path.isdir(path):
        os.mkdir(path)

TEMPLATE_DIR = os.path.join(ROOT_DIR, 'templates')

env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))

# Looping on every yaml file in the "steps" directory
for filename in os.listdir(STEP_DIR):
    print "processing %s" % filename
    root, _ = os.path.splitext(filename)
    fullpath = os.path.join(STEP_DIR, filename)
    build_file = os.path.join(BUILD_DIR, "%s.html" % root)
    data = yaml.load(open(fullpath, encoding='utf8'))

    if data:
        # picking the intro data and make a markdown transform
        if 'intro' in data:
            data['intro'] = markdown.markdown(data['intro'])

        # pick the right template
        template_name = 'step.html'
        if 'template' in data:
            template_name = data['template']
        current_template = env.get_template(template_name)

        # build html file
        with open(build_file, 'w', encoding='utf8') as fd:
            fd.write(current_template.render(**data))

# To be done only if everything's all right
shutil.rmtree(ASSET_DEST_DIR)
shutil.copytree(ASSET_SOURCE_DIR, ASSET_DEST_DIR)
