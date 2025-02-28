g_base_prompt = f"using pandas 3 and python 3.10+ to clean data in jupyter lab."
g_ds_prompt = f"You are a data scientist {g_base_prompt}"
g_pf_prompt = f"You are a professor of data science teaching a class on {g_base_prompt}." 

# ai helper prompts
g_unique_set_prefix = "for column named"
g_col_check_prefix = "check column named"
g_code_prefix = "write code to"

# non-ai prompts
g_summarize_statement = "summarize table"

# button prompts
g_add_cell_statement = "add cell"
g_copy_last_statement = "copy it"
g_run_last_statement = "now run it"
g_revert_df_statement = "revert dataframe"