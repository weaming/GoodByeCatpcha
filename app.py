#!/usr/bin/env python3
# Author    : weaming
# Mail      : garden.yuen@gmail.com
# Created   : 2020-05-09 22:41:41

import os
from sanic import Sanic
from json_api.magic_sanic import MagicSanic
from goodbyecaptcha.solver import Solver

app = Sanic()
magic = MagicSanic()
magic.set_app(app)


async def index(
    request, pageurl, sitekey,
):
    method = 'images'  # 'audio'
    args = ["--timeout 5"]
    options = {"ignoreHTTPSErrors": True, "method": method, "args": args}
    client = Solver(pageurl, sitekey, options=options,)
    return await client.start()


magic.add_route("/", index)

if __name__ == "__main__":
    debug = bool(os.getenv("DEBUG"))
    app.run(host="0.0.0.0", port=5000, debug=debug)
