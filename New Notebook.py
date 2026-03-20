# Databricks notebook source
# /// script
# [tool.databricks.environment]
# environment_version = "4"
# ///


notebook_name = dbutils.notebook.entry_point.getDbutils().notebook().getContext()
print(notebook_name)

# COMMAND ----------

# Test
