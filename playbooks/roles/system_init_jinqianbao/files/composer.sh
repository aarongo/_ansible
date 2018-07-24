#!/usr/bin/env bash

EXEC_HOME=/usr/local/bin/composer

${EXEC_HOME} config -g github-oauth.github.com "6afb356a8bff76f2722c99520c563bd49b40147c"
${EXEC_HOME} config -g repo.packagist composer https://packagist.phpcomposer.com
${EXEC_HOME} global require "fxp/composer-asset-plugin:^1.3.0"