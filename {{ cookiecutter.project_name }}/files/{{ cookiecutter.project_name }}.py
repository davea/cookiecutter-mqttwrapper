#!/usr/bin/env python

from dotenv import load_dotenv

load_dotenv()

from mqttwrapper import run_script


def callback(topic, payload, *args, **kwargs):
    print(f"Received {payload} on topic {topic}", flush=True)


def main():
    run_script(callback)


if __name__ == "__main__":
    main()
