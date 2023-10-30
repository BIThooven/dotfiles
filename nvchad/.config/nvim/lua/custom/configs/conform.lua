local M = {}

M.opts = {
	format_on_save = {
		timeout_ms = 500,
		lsp_fallback = true,
	},
	formatters_by_ft = {
		cs = { "csharpier" },
		lua = { "stylua" },
		markdown = { "prettier", "injected" },
		json = { "prettier" },
		xml = { "xmlformat" },
	},
}

return M
