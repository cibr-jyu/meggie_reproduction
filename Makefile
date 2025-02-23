.PHONY: format
format:
	black meggie_reproduction

.PHONY: check
check:
	black --check meggie_reproduction
	pylama meggie_reproduction

.PHONY: test
test:
	pytest -s
