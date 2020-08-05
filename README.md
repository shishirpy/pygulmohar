# Introduction

This is the python client library of the [`gulmohar-server`](https://github.com/shishirpy/gulmohar-server). The repository contains both the client and worker APIs.

# Why

1. Why do we need the [`gulmohar-server`](https://github.com/shishirpy/gulmohar-server)? 
    * I want it to be easy to serve your machine learning models with anyone. I have generally done that with [`flask`](https://flask.palletsprojects.com/). But then you do have to learn `flask` and how to organize your projects. With the worker and client APIs I hope that the learning need to serve your models will be minimal.
1. If you have multiple models on different problems it should be easy to expose your models using service names each having its own code base.

# Getting Started

The run the [`gulmohar-server`](https://github.com/shishirpy/gulmohar-server) in the docker container. If all went well, the `gulmohar-server` will be running on port `5555` on localhost. 



