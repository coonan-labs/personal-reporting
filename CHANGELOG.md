# CHANGELOG


## v1.0.0 (2026-11-28)

### Bug Fixes

- Add --cov=pipelines flag to generate coverage.xml
  ([#116](https://github.com/michaelconan/personal-reporting-pipelines/pull/116),
  [`708875d`](https://github.com/michaelconan/personal-reporting-pipelines/commit/708875d0408dca1173af0fdb7dd9aace031b81d9))

- Add airflow home to supervisor env
  ([`2cf96ea`](https://github.com/michaelconan/personal-reporting-pipelines/commit/2cf96ead2c72374ff8c5f16bad191d1bbbefe4b1))

- Add back chown execute
  ([`a157697`](https://github.com/michaelconan/personal-reporting-pipelines/commit/a157697f747ad1dce50501ad502ab8ff0d36e7f7))

- Add contraints from freeze
  ([`db8ae6d`](https://github.com/michaelconan/personal-reporting-pipelines/commit/db8ae6d67c9771a19bea0b42f573d2d33f187733))

- Add dbt.html to gitignore
  ([#79](https://github.com/michaelconan/personal-reporting-pipelines/pull/79),
  [`c624533`](https://github.com/michaelconan/personal-reporting-pipelines/commit/c62453352e8dd47580bb5f5e576d0914322c9a30))

- Add dbt.html to gitignore
  ([#76](https://github.com/michaelconan/personal-reporting-pipelines/pull/76),
  [`ea2be76`](https://github.com/michaelconan/personal-reporting-pipelines/commit/ea2be765482ce411e6ddc980ca58146a4de22e60))

- Add dbt.html to gitignore
  ([#75](https://github.com/michaelconan/personal-reporting-pipelines/pull/75),
  [`a72ce18`](https://github.com/michaelconan/personal-reporting-pipelines/commit/a72ce18984fe19c2e72d584f69ce713c1f4b26d0))

- Address opencode review on PR #172; disable dlt telemetry project-wide
  ([#172](https://github.com/michaelconan/personal-reporting-pipelines/pull/172),
  [`48afdff`](https://github.com/michaelconan/personal-reporting-pipelines/commit/48afdff3889c9fd255b2d8599e57e31c5e40581c))

- Address PR #151 review findings and Databricks build
  ([#151](https://github.com/michaelconan/personal-reporting-pipelines/pull/151),
  [`94e7e4d`](https://github.com/michaelconan/personal-reporting-pipelines/commit/94e7e4d7dea0628a86eba9541c69832dbee32d00))

- Archived sweep via Search API with archived:true in POST body
  ([#172](https://github.com/michaelconan/personal-reporting-pipelines/pull/172),
  [`48afdff`](https://github.com/michaelconan/personal-reporting-pipelines/commit/48afdff3889c9fd255b2d8599e57e31c5e40581c))

- Correct security workflow follow-up
  ([#139](https://github.com/michaelconan/personal-reporting-pipelines/pull/139),
  [`4c37c6f`](https://github.com/michaelconan/personal-reporting-pipelines/commit/4c37c6f89c1583682dd5818ac2b045070d9cb020))

- Drop undocumented meetings properties that break archived list endpoint
  ([#172](https://github.com/michaelconan/personal-reporting-pipelines/pull/172),
  [`48afdff`](https://github.com/michaelconan/personal-reporting-pipelines/commit/48afdff3889c9fd255b2d8599e57e31c5e40581c))

- Improve GCP credentials handling in GitHub Actions workflows
  ([`de75498`](https://github.com/michaelconan/personal-reporting-pipelines/commit/de75498cf64b3d9ad2591f6c9d57e56147819ce5))

- Mask refresh token in subprocess error output
  ([#110](https://github.com/michaelconan/personal-reporting-pipelines/pull/110),
  [`0413d9e`](https://github.com/michaelconan/personal-reporting-pipelines/commit/0413d9e1c7388c308069d8005b767d0ca978a175))

- Normalize line endings according to gitattributes
  ([`8a7e02b`](https://github.com/michaelconan/personal-reporting-pipelines/commit/8a7e02b97175c905ebffd6a71c092dd1c0463786))

- Prevent op template/stdin conflict by closing stdin
  ([#114](https://github.com/michaelconan/personal-reporting-pipelines/pull/114),
  [`5b51d50`](https://github.com/michaelconan/personal-reporting-pipelines/commit/5b51d50ae10135ed9422fed95c0995f31c9ce5fb))

- Recompile gh-aw workflows with v0.74.8 (retire v0.71.1)
  ([`4909219`](https://github.com/michaelconan/personal-reporting-pipelines/commit/4909219ca2e0d8696a8b34ebda5fbdf6d3e92c95))

- Remove invalid comments in jinja commands, update lint config
  ([#88](https://github.com/michaelconan/personal-reporting-pipelines/pull/88),
  [`a478ae8`](https://github.com/michaelconan/personal-reporting-pipelines/commit/a478ae8288d0e9ab67702da564fcde029e3fe0aa))

- Remove invalid comments in jinja commands, update lint config
  ([`51ba61d`](https://github.com/michaelconan/personal-reporting-pipelines/commit/51ba61dbb7f37b843c9f902588a7f0f6c753eb91))

- Remove invalid make echo suppression
  ([#88](https://github.com/michaelconan/personal-reporting-pipelines/pull/88),
  [`a478ae8`](https://github.com/michaelconan/personal-reporting-pipelines/commit/a478ae8288d0e9ab67702da564fcde029e3fe0aa))

- Remove invalid make echo suppression
  ([`34e1c88`](https://github.com/michaelconan/personal-reporting-pipelines/commit/34e1c88a95096ea7bd078ee58689ad6ca9c3dda5))

- Remove unused import from conftest.py
  ([`ec4b54e`](https://github.com/michaelconan/personal-reporting-pipelines/commit/ec4b54ea1c9474966ea6af820c25b270ff48b421))

- Replace QUALIFY with DISTINCT ON in duckdb__deduplicate to fix type binding crash
  ([`1958bc1`](https://github.com/michaelconan/personal-reporting-pipelines/commit/1958bc1ac909d002d06e7dac48bb75318c9f77b5))

- Resolve dbt contract validation failures and test fixture paths
  ([#146](https://github.com/michaelconan/personal-reporting-pipelines/pull/146),
  [`f9fede0`](https://github.com/michaelconan/personal-reporting-pipelines/commit/f9fede0c964c71a5e8dfe7ef6a441dd42ad92c4f))

- Resolve HubSpot pipeline test fixtures and CI improvements
  ([`4eae1f0`](https://github.com/michaelconan/personal-reporting-pipelines/commit/4eae1f0bb7d9113103619c05ba1543d8f56db9cb))

- Tolerate missing _deleted columns and skip archived sweep in fixture export
  ([#172](https://github.com/michaelconan/personal-reporting-pipelines/pull/172),
  [`48afdff`](https://github.com/michaelconan/personal-reporting-pipelines/commit/48afdff3889c9fd255b2d8599e57e31c5e40581c))

- Update CI workflow steps and permissions
  ([`057c8f8`](https://github.com/michaelconan/personal-reporting-pipelines/commit/057c8f81669366730c18bbb9866175ffccbf307e))

- Update db connection to airflow home
  ([`7225c98`](https://github.com/michaelconan/personal-reporting-pipelines/commit/7225c989165d3c6b8977f5d3155a09b51eef0bba))

- Update dbt directory detection
  ([`e30e216`](https://github.com/michaelconan/personal-reporting-pipelines/commit/e30e216c855c1e4d15bffc35f4bf26921fe5f948))

- Update dbt tests and ci workflows
  ([`cf5a52c`](https://github.com/michaelconan/personal-reporting-pipelines/commit/cf5a52c77d7730f66dfaaee99c395763d0334337))

- Update dependency to reduce google components
  ([`935740d`](https://github.com/michaelconan/personal-reporting-pipelines/commit/935740d092d1560d8e4997ff7d0ddb64289106a5))

- Update docs workflow
  ([`51299bf`](https://github.com/michaelconan/personal-reporting-pipelines/commit/51299bf97871d7e18fcf750f46399f55cc7c3e5a))

- Update docs workflow
  ([`f22d3a9`](https://github.com/michaelconan/personal-reporting-pipelines/commit/f22d3a9bc3b05098e9a7c3874d1cec3f8919514b))

- Update executor and startup
  ([`2a4444a`](https://github.com/michaelconan/personal-reporting-pipelines/commit/2a4444a8a0ff643139e6917221d009751af99be9))

- Update make source macro and uses across the staging models
  ([#88](https://github.com/michaelconan/personal-reporting-pipelines/pull/88),
  [`a478ae8`](https://github.com/michaelconan/personal-reporting-pipelines/commit/a478ae8288d0e9ab67702da564fcde029e3fe0aa))

- Update make source macro and uses across the staging models
  ([#86](https://github.com/michaelconan/personal-reporting-pipelines/pull/86),
  [`ff61b0c`](https://github.com/michaelconan/personal-reporting-pipelines/commit/ff61b0c3d00518e41403673b56d3eee353b50ab4))

- Update make source macro and uses across the staging models
  ([#84](https://github.com/michaelconan/personal-reporting-pipelines/pull/84),
  [`df2e77a`](https://github.com/michaelconan/personal-reporting-pipelines/commit/df2e77a49307ba18f72581a87ca3389960aff436))

- Update make source macro and uses across the staging models
  ([`c6b110b`](https://github.com/michaelconan/personal-reporting-pipelines/commit/c6b110bdba92271c949d4a2e5ae5745eb390c010))

- Update mart models and data tests
  ([#88](https://github.com/michaelconan/personal-reporting-pipelines/pull/88),
  [`a478ae8`](https://github.com/michaelconan/personal-reporting-pipelines/commit/a478ae8288d0e9ab67702da564fcde029e3fe0aa))

- Update mart models and data tests
  ([#86](https://github.com/michaelconan/personal-reporting-pipelines/pull/86),
  [`ff61b0c`](https://github.com/michaelconan/personal-reporting-pipelines/commit/ff61b0c3d00518e41403673b56d3eee353b50ab4))

- Update mart models and data tests
  ([#84](https://github.com/michaelconan/personal-reporting-pipelines/pull/84),
  [`df2e77a`](https://github.com/michaelconan/personal-reporting-pipelines/commit/df2e77a49307ba18f72581a87ca3389960aff436))

- Update mart models and data tests
  ([`3576e2a`](https://github.com/michaelconan/personal-reporting-pipelines/commit/3576e2a828b62a29a81754b026bdb20333723478))

- Update modules for unit tests
  ([`02a4696`](https://github.com/michaelconan/personal-reporting-pipelines/commit/02a46968755135d105ec56364bf0067579bdf619))

- Update path for copying static_index.html in Makefile
  ([`2d95753`](https://github.com/michaelconan/personal-reporting-pipelines/commit/2d95753bdc57434f59d6b968ec8f97ca1286beff))

- Update post create command@
  ([`ecf18b9`](https://github.com/michaelconan/personal-reporting-pipelines/commit/ecf18b987ea08526cbb0ee5b887475599070e59e))

- Update procfile web command for worker timeout
  ([`7f26de7`](https://github.com/michaelconan/personal-reporting-pipelines/commit/7f26de712e4aa695019c32236d46f55009d644fe))

- Update step name for clarity
  ([`c6c377a`](https://github.com/michaelconan/personal-reporting-pipelines/commit/c6c377aa81f4f1aa4c26387c3acd73c168de99a9))

- Update supervisor and startup scripts
  ([`a16efbf`](https://github.com/michaelconan/personal-reporting-pipelines/commit/a16efbf82be0fb3087f1e32f4803fa08395146d5))

- Update to clean up for precommit
  ([`ed13d6d`](https://github.com/michaelconan/personal-reporting-pipelines/commit/ed13d6d877f2cf4c9be362a78a036a68fa0fe592))

- Update to install without constraints
  ([`ca0bb01`](https://github.com/michaelconan/personal-reporting-pipelines/commit/ca0bb010e79fc959ad117a55c25dcc0b9cad8d66))

- Use heredoc for GCP service account key to prevent line break issues
  ([`55d7756`](https://github.com/michaelconan/personal-reporting-pipelines/commit/55d77569bcc799445750e25298dc009c380867e4))

- **agentcontainer**: Point zen-proxy base URLs at /go/v1 and pin default model
  ([#148](https://github.com/michaelconan/personal-reporting-pipelines/pull/148),
  [`80001b2`](https://github.com/michaelconan/personal-reporting-pipelines/commit/80001b2993e188ec6be384911b7b0413e873d774))

- **agentcontainer**: Switch default model to qwen-3.8-flash
  ([#148](https://github.com/michaelconan/personal-reporting-pipelines/pull/148),
  [`80001b2`](https://github.com/michaelconan/personal-reporting-pipelines/commit/80001b2993e188ec6be384911b7b0413e873d774))

- **ci**: Correct indentation of mock-steps workflow step
  ([#169](https://github.com/michaelconan/personal-reporting-pipelines/pull/169),
  [`85e5850`](https://github.com/michaelconan/personal-reporting-pipelines/commit/85e58501c3bb503ede5d7a9793d4dee9217c8680))

- **ci**: Disable interactive opencode permission prompts
  ([#162](https://github.com/michaelconan/personal-reporting-pipelines/pull/162),
  [`6dd85a2`](https://github.com/michaelconan/personal-reporting-pipelines/commit/6dd85a211670a5ca3fc4b35a3506766da81b67c5))

- **ci**: Lock down read-only opencode agents
  ([#162](https://github.com/michaelconan/personal-reporting-pipelines/pull/162),
  [`6dd85a2`](https://github.com/michaelconan/personal-reporting-pipelines/commit/6dd85a211670a5ca3fc4b35a3506766da81b67c5))

- **ci**: Pin target env through op run and validate schemas
  ([#162](https://github.com/michaelconan/personal-reporting-pipelines/pull/162),
  [`6dd85a2`](https://github.com/michaelconan/personal-reporting-pipelines/commit/6dd85a211670a5ca3fc4b35a3506766da81b67c5))

- **ci**: Rely on environment DBT_TARGET for scheduled runs
  ([#162](https://github.com/michaelconan/personal-reporting-pipelines/pull/162),
  [`6dd85a2`](https://github.com/michaelconan/personal-reporting-pipelines/commit/6dd85a211670a5ca3fc4b35a3506766da81b67c5))

- **ci**: Resolve lint and formatting failures
  ([`4ca6dfb`](https://github.com/michaelconan/personal-reporting-pipelines/commit/4ca6dfba3bea3ca6f24c9ba68e163623ae104f64))

- **ci**: Run dlt and dbt workflows against production
  ([#162](https://github.com/michaelconan/personal-reporting-pipelines/pull/162),
  [`6dd85a2`](https://github.com/michaelconan/personal-reporting-pipelines/commit/6dd85a211670a5ca3fc4b35a3506766da81b67c5))

- **ci**: Scope opencode permissions for read-only reviews
  ([#162](https://github.com/michaelconan/personal-reporting-pipelines/pull/162),
  [`6dd85a2`](https://github.com/michaelconan/personal-reporting-pipelines/commit/6dd85a211670a5ca3fc4b35a3506766da81b67c5))

- **ci**: Standardize dbt target and schema environment
  ([#162](https://github.com/michaelconan/personal-reporting-pipelines/pull/162),
  [`6dd85a2`](https://github.com/michaelconan/personal-reporting-pipelines/commit/6dd85a211670a5ca3fc4b35a3506766da81b67c5))

- **ci**: Update dbt test to run against test target
  ([#151](https://github.com/michaelconan/personal-reporting-pipelines/pull/151),
  [`94e7e4d`](https://github.com/michaelconan/personal-reporting-pipelines/commit/94e7e4d7dea0628a86eba9541c69832dbee32d00))

- **databricks**: Address fifth opencode review
  ([`5e67c69`](https://github.com/michaelconan/personal-reporting-pipelines/commit/5e67c69a8c7d4d9d5633645caff21b1b05b4b5d6))

- **databricks**: Address fourth opencode review
  ([`7cd66bd`](https://github.com/michaelconan/personal-reporting-pipelines/commit/7cd66bdf8eaed0b293fab9a88b2132050c0d8b0e))

- **databricks**: Address opencode review on warehouse start retry
  ([`6ab4581`](https://github.com/michaelconan/personal-reporting-pipelines/commit/6ab4581118634ec0d814b359b59f3d2c2bb36062))

- **databricks**: Address sixth opencode review
  ([`06d7146`](https://github.com/michaelconan/personal-reporting-pipelines/commit/06d71469c154466fc81e752d69003bb7d5e9dcf4))

- **databricks**: Fix launched flag so STOPPED grace period actually runs
  ([`fc5d079`](https://github.com/michaelconan/personal-reporting-pipelines/commit/fc5d079bb7a229c0cc2498647dde490bac6efc61))

- **databricks**: Make the 15-minute bound real and tolerate duplicate starts
  ([`137c732`](https://github.com/michaelconan/personal-reporting-pipelines/commit/137c732a05759904aca6d4d0da54b50fe9c5a56b))

- **databricks**: Retry warehouse start on transient capacity errors
  ([`d9852d2`](https://github.com/michaelconan/personal-reporting-pipelines/commit/d9852d261c29c9299e7dbdbbd04c5eccca41f42f))

- **dbt**: Address review feedback on fct_health_data_gaps
  ([#169](https://github.com/michaelconan/personal-reporting-pipelines/pull/169),
  [`85e5850`](https://github.com/michaelconan/personal-reporting-pipelines/commit/85e58501c3bb503ede5d7a9793d4dee9217c8680))

- **dbt**: Cast session timestamps to timestamp in fct_health_session_v1
  ([#169](https://github.com/michaelconan/personal-reporting-pipelines/pull/169),
  [`85e5850`](https://github.com/michaelconan/personal-reporting-pipelines/commit/85e58501c3bb503ede5d7a9793d4dee9217c8680))

- **dbt**: Pin TZ=UTC for the mock build
  ([#169](https://github.com/michaelconan/personal-reporting-pipelines/pull/169),
  [`85e5850`](https://github.com/michaelconan/personal-reporting-pipelines/commit/85e58501c3bb503ede5d7a9793d4dee9217c8680))

- **dbt**: Quote _dlt_loads per-part in source freshness query
  ([#158](https://github.com/michaelconan/personal-reporting-pipelines/pull/158),
  [`88ea661`](https://github.com/michaelconan/personal-reporting-pipelines/commit/88ea661f80a59175cfa9a6045050f55ba8592e62))

- **dbt**: Raise weekly screen_minutes test max to 2500
  ([`92a3334`](https://github.com/michaelconan/personal-reporting-pipelines/commit/92a3334c7397840c86af319a3b61e080e9501d42))

- **dbt**: Remove optional nap metadata from sleep models
  ([#162](https://github.com/michaelconan/personal-reporting-pipelines/pull/162),
  [`6dd85a2`](https://github.com/michaelconan/personal-reporting-pipelines/commit/6dd85a211670a5ca3fc4b35a3506766da81b67c5))

- **dbt**: Scope source freshness to tables expected to be fresh
  ([`e78d9f0`](https://github.com/michaelconan/personal-reporting-pipelines/commit/e78d9f08bbb9b6306418e82358e8a3553dcb3e52))

- **fct_engagement_v1**: Cast engagement_id to varchar to match contract
  ([`5073312`](https://github.com/michaelconan/personal-reporting-pipelines/commit/50733127970b9bc77e17d5bd1ca324ee057c6de9))

- **google-health**: Add civil timestamp handling for refresh without end date
  ([`0d74db9`](https://github.com/michaelconan/personal-reporting-pipelines/commit/0d74db9dba272acc7fb4464aa5369002971b7c47))

- **google-health**: Clarify cursor date handling; pin filter in live test
  ([#158](https://github.com/michaelconan/personal-reporting-pipelines/pull/158),
  [`88ea661`](https://github.com/michaelconan/personal-reporting-pipelines/commit/88ea661f80a59175cfa9a6045050f55ba8592e62))

- **google-health**: Update e2e test timeout and add API links
  ([`66b3003`](https://github.com/michaelconan/personal-reporting-pipelines/commit/66b30037a24d533bc6a7d429537144e74fe96bc6))

- **google-health**: Widen exercise civil filter to cover UTC/civil gap
  ([#158](https://github.com/michaelconan/personal-reporting-pipelines/pull/158),
  [`88ea661`](https://github.com/michaelconan/personal-reporting-pipelines/commit/88ea661f80a59175cfa9a6045050f55ba8592e62))

- **marts**: Cast engagement_id as string in fct_engagement_v1 (Databricks
  ([#151](https://github.com/michaelconan/personal-reporting-pipelines/pull/151),
  [`94e7e4d`](https://github.com/michaelconan/personal-reporting-pipelines/commit/94e7e4d7dea0628a86eba9541c69832dbee32d00))

- **mise**: Update location of op and mise run scripts
  ([#151](https://github.com/michaelconan/personal-reporting-pipelines/pull/151),
  [`94e7e4d`](https://github.com/michaelconan/personal-reporting-pipelines/commit/94e7e4d7dea0628a86eba9541c69832dbee32d00))

- **pipelines**: Improve credential handling and test structure
  ([`2f05c57`](https://github.com/michaelconan/personal-reporting-pipelines/commit/2f05c57b11dc0cbd1edb3b5b851a17c4a2bb00a4))

- **pipelines**: Synthesize HubSpot fixture cursor for single-page captures
  ([#169](https://github.com/michaelconan/personal-reporting-pipelines/pull/169),
  [`85e5850`](https://github.com/michaelconan/personal-reporting-pipelines/commit/85e58501c3bb503ede5d7a9793d4dee9217c8680))

- **pipelines**: Validate target and schema pairs
  ([#162](https://github.com/michaelconan/personal-reporting-pipelines/pull/162),
  [`6dd85a2`](https://github.com/michaelconan/personal-reporting-pipelines/commit/6dd85a211670a5ca3fc4b35a3506766da81b67c5))

- **review**: Exercise include_steps in CI and surface total steps outages
  ([#169](https://github.com/michaelconan/personal-reporting-pipelines/pull/169),
  [`85e5850`](https://github.com/michaelconan/personal-reporting-pipelines/commit/85e58501c3bb503ede5d7a9793d4dee9217c8680))

- **review**: Follow-ups from the 13:36 review
  ([#169](https://github.com/michaelconan/personal-reporting-pipelines/pull/169),
  [`85e5850`](https://github.com/michaelconan/personal-reporting-pipelines/commit/85e58501c3bb503ede5d7a9793d4dee9217c8680))

- **review**: GAPFIX fixture block rows and check-mode-proof fixture test
  ([#169](https://github.com/michaelconan/personal-reporting-pipelines/pull/169),
  [`85e5850`](https://github.com/michaelconan/personal-reporting-pipelines/commit/85e58501c3bb503ede5d7a9793d4dee9217c8680))

- **review**: List var, array gap_types, revert cursor synthesis
  ([#169](https://github.com/michaelconan/personal-reporting-pipelines/pull/169),
  [`85e5850`](https://github.com/michaelconan/personal-reporting-pipelines/commit/85e58501c3bb503ede5d7a9793d4dee9217c8680))

- **security**: Harden OpenCode workflows and restore Fitbit
  ([#139](https://github.com/michaelconan/personal-reporting-pipelines/pull/139),
  [`4c37c6f`](https://github.com/michaelconan/personal-reporting-pipelines/commit/4c37c6f89c1583682dd5818ac2b045070d9cb020))

- **security**: Scrub dotted fixture keys
  ([#139](https://github.com/michaelconan/personal-reporting-pipelines/pull/139),
  [`4c37c6f`](https://github.com/michaelconan/personal-reporting-pipelines/commit/4c37c6f89c1583682dd5818ac2b045070d9cb020))

- **semantic**: Correct count-habit completion and habit dimension
  ([#144](https://github.com/michaelconan/personal-reporting-pipelines/pull/144),
  [`35c2734`](https://github.com/michaelconan/personal-reporting-pipelines/commit/35c273413a8a726a82ef31de7dc33f120860dce5))

### Build System

- **dbt**: Upgrade to dbt 2.x and strengthen macro governance
  ([#144](https://github.com/michaelconan/personal-reporting-pipelines/pull/144),
  [`35c2734`](https://github.com/michaelconan/personal-reporting-pipelines/commit/35c273413a8a726a82ef31de7dc33f120860dce5))

### Chores

- Add doc updater agentic workflow
  ([#114](https://github.com/michaelconan/personal-reporting-pipelines/pull/114),
  [`5b51d50`](https://github.com/michaelconan/personal-reporting-pipelines/commit/5b51d50ae10135ed9422fed95c0995f31c9ce5fb))

- Add environment to docs workflow
  ([#79](https://github.com/michaelconan/personal-reporting-pipelines/pull/79),
  [`c624533`](https://github.com/michaelconan/personal-reporting-pipelines/commit/c62453352e8dd47580bb5f5e576d0914322c9a30))

- Add environment to docs workflow
  ([#76](https://github.com/michaelconan/personal-reporting-pipelines/pull/76),
  [`ea2be76`](https://github.com/michaelconan/personal-reporting-pipelines/commit/ea2be765482ce411e6ddc980ca58146a4de22e60))

- Add environment to docs workflow
  ([#75](https://github.com/michaelconan/personal-reporting-pipelines/pull/75),
  [`a72ce18`](https://github.com/michaelconan/personal-reporting-pipelines/commit/a72ce18984fe19c2e72d584f69ce713c1f4b26d0))

- Add OP_SERVICE_ACCOUNT_TOKEN to environment variables in workflow files
  ([`e441d6a`](https://github.com/michaelconan/personal-reporting-pipelines/commit/e441d6a8bdf728d8a02860da5261c6a0413a64cb))

- Add sandbox env, e2e cleanup helpers, and fixture router
  ([#151](https://github.com/michaelconan/personal-reporting-pipelines/pull/151),
  [`94e7e4d`](https://github.com/michaelconan/personal-reporting-pipelines/commit/94e7e4d7dea0628a86eba9541c69832dbee32d00))

- Consolidate tool configs into pyproject.toml and fix pre-commit
  ([`13eca48`](https://github.com/michaelconan/personal-reporting-pipelines/commit/13eca48a635807e06a3cc6fdca821ef73061346c))

- Disable dlt telemetry (telemetry.scalevector.ai) for all pipeline runs
  ([#172](https://github.com/michaelconan/personal-reporting-pipelines/pull/172),
  [`48afdff`](https://github.com/michaelconan/personal-reporting-pipelines/commit/48afdff3889c9fd255b2d8599e57e31c5e40581c))

- Docs workflow
  ([`647b7ee`](https://github.com/michaelconan/personal-reporting-pipelines/commit/647b7ee5616adcfdca7a2bfdb8574f06aa0b18f5))

- Fix devcontainer, lockfile, and test issues for Python 3.13
  ([`24c7707`](https://github.com/michaelconan/personal-reporting-pipelines/commit/24c7707b7f5124ff6c822f881a766ea590c061b8))

- Fix output option for latest dbt-coverage version
  ([#79](https://github.com/michaelconan/personal-reporting-pipelines/pull/79),
  [`c624533`](https://github.com/michaelconan/personal-reporting-pipelines/commit/c62453352e8dd47580bb5f5e576d0914322c9a30))

- Fix workflow dependencies and pipeline logging
  ([#79](https://github.com/michaelconan/personal-reporting-pipelines/pull/79),
  [`c624533`](https://github.com/michaelconan/personal-reporting-pipelines/commit/c62453352e8dd47580bb5f5e576d0914322c9a30))

- Harden GitHub Actions workflows (#174)
  ([#175](https://github.com/michaelconan/personal-reporting-pipelines/pull/175),
  [`9fcf494`](https://github.com/michaelconan/personal-reporting-pipelines/commit/9fcf494be0c1e38159fe0db67965147ed3323c79))

- Remove dbt cloud package from pipenv
  ([`d7e4978`](https://github.com/michaelconan/personal-reporting-pipelines/commit/d7e4978cc496256c9d1974436e63d83e341a34c0))

- Remove push trigger from ci workflow
  ([`4c6710b`](https://github.com/michaelconan/personal-reporting-pipelines/commit/4c6710b4c330b5dff54d2fbe89abe21f0a970178))

- Switch weekly doc updater engine from copilot to gemini
  ([#116](https://github.com/michaelconan/personal-reporting-pipelines/pull/116),
  [`708875d`](https://github.com/michaelconan/personal-reporting-pipelines/commit/708875d0408dca1173af0fdb7dd9aace031b81d9))

- Update 1password step in actions
  ([`d4048d8`](https://github.com/michaelconan/personal-reporting-pipelines/commit/d4048d881601f636bef4dcaa62326f7c9de3a3ef))

- Update CI test workflow to remove separate unneeded coverage step
  ([`0330592`](https://github.com/michaelconan/personal-reporting-pipelines/commit/033059228da5e9dd21ce4dc430388c64252c8d8f))

- Update dbt dag paths
  ([`f70a6c6`](https://github.com/michaelconan/personal-reporting-pipelines/commit/f70a6c65c9a54bde012aecc627098daed206d04b))

- Update dbt targets and workflow for coverage
  ([#79](https://github.com/michaelconan/personal-reporting-pipelines/pull/79),
  [`c624533`](https://github.com/michaelconan/personal-reporting-pipelines/commit/c62453352e8dd47580bb5f5e576d0914322c9a30))

- Update e2e test config and gemini actions
  ([#88](https://github.com/michaelconan/personal-reporting-pipelines/pull/88),
  [`a478ae8`](https://github.com/michaelconan/personal-reporting-pipelines/commit/a478ae8288d0e9ab67702da564fcde029e3fe0aa))

- Update e2e test config and gemini actions
  ([#86](https://github.com/michaelconan/personal-reporting-pipelines/pull/86),
  [`ff61b0c`](https://github.com/michaelconan/personal-reporting-pipelines/commit/ff61b0c3d00518e41403673b56d3eee353b50ab4))

- Update e2e test config and gemini actions
  ([`8da9b54`](https://github.com/michaelconan/personal-reporting-pipelines/commit/8da9b54b0921e036a50b83790e837bf3219658f9))

- Update gemini workflow to skip for dependabot
  ([`db039b9`](https://github.com/michaelconan/personal-reporting-pipelines/commit/db039b9f0fef367dbaf59db2e1ea6502c89d0714))

- Update GitHub Actions to Node.js 24 and replace Gemini with Copilot
  ([#114](https://github.com/michaelconan/personal-reporting-pipelines/pull/114),
  [`5b51d50`](https://github.com/michaelconan/personal-reporting-pipelines/commit/5b51d50ae10135ed9422fed95c0995f31c9ce5fb))

- Update makefile and CI test workflow for codecov reporting
  ([`483c3df`](https://github.com/michaelconan/personal-reporting-pipelines/commit/483c3df155dd20f4f213991e5e5491f25139a841))

- Update weekly-doc-updater workflow to use Google Gemini
  ([#116](https://github.com/michaelconan/personal-reporting-pipelines/pull/116),
  [`708875d`](https://github.com/michaelconan/personal-reporting-pipelines/commit/708875d0408dca1173af0fdb7dd9aace031b81d9))

- Upgrade to Python 3.13 and fix CI install
  ([`fda6e13`](https://github.com/michaelconan/personal-reporting-pipelines/commit/fda6e1374d9764a8a32a39930d488a1bcea3e027))

- Use --cov without package arg, delegate source to pyproject.toml
  ([#116](https://github.com/michaelconan/personal-reporting-pipelines/pull/116),
  [`708875d`](https://github.com/michaelconan/personal-reporting-pipelines/commit/708875d0408dca1173af0fdb7dd9aace031b81d9))

- **agents**: Migrate editor rules and add opencode automation plus dlthub skills
  ([#139](https://github.com/michaelconan/personal-reporting-pipelines/pull/139),
  [`4c37c6f`](https://github.com/michaelconan/personal-reporting-pipelines/commit/4c37c6f89c1583682dd5818ac2b045070d9cb020))

- **bouncer**: Remove bouncer from dbt test workflow and change check severity
  ([#144](https://github.com/michaelconan/personal-reporting-pipelines/pull/144),
  [`35c2734`](https://github.com/michaelconan/personal-reporting-pipelines/commit/35c273413a8a726a82ef31de7dc33f120860dce5))

- **bouncer**: Remove bouncer from dbt test workflow and change check severity
  ([#140](https://github.com/michaelconan/personal-reporting-pipelines/pull/140),
  [`23acc0f`](https://github.com/michaelconan/personal-reporting-pipelines/commit/23acc0f3e90a0ad2bebca0e626450bebfe504963))

- **claude**: Remove stale pipenv python rule
  ([#148](https://github.com/michaelconan/personal-reporting-pipelines/pull/148),
  [`80001b2`](https://github.com/michaelconan/personal-reporting-pipelines/commit/80001b2993e188ec6be384911b7b0413e873d774))

- **deps**: Bump actions/cache/save from 5.0.5 to 6.1.0
  ([#177](https://github.com/michaelconan/personal-reporting-pipelines/pull/177),
  [`6004bc8`](https://github.com/michaelconan/personal-reporting-pipelines/commit/6004bc8812bbac60de6a6f3b3df21ced15e6502e))

- **deps**: Bump actions/checkout from 6.0.2 to 7.0.1
  ([#176](https://github.com/michaelconan/personal-reporting-pipelines/pull/176),
  [`53f508c`](https://github.com/michaelconan/personal-reporting-pipelines/commit/53f508c0dc4bb5c57020d91c722075716ab0578f))

- **deps**: Bump actions/download-artifact from 8.0.1 to 8.0.2
  ([#178](https://github.com/michaelconan/personal-reporting-pipelines/pull/178),
  [`da480b5`](https://github.com/michaelconan/personal-reporting-pipelines/commit/da480b556bf25e983e6ec34f19e528972dd6ce5b))

- **deps**: Bump aiohttp in the pip group across 1 directory
  ([`b722588`](https://github.com/michaelconan/personal-reporting-pipelines/commit/b722588f455df12b3c1409f8d92ebead4577ee48))

- **deps**: Bump anyio in the uv group across 1 directory
  ([#143](https://github.com/michaelconan/personal-reporting-pipelines/pull/143),
  [`786621e`](https://github.com/michaelconan/personal-reporting-pipelines/commit/786621e767a454ec48c1384157ed853654cfb355))

- **deps**: Bump deepdiff in the pip group across 1 directory
  ([`6c7a995`](https://github.com/michaelconan/personal-reporting-pipelines/commit/6c7a9957f35f454105cfab80df4704da2ad814a9))

- **deps**: Bump fsspec and multidict, hold oauthlib below 4.0.0
  ([#158](https://github.com/michaelconan/personal-reporting-pipelines/pull/158),
  [`88ea661`](https://github.com/michaelconan/personal-reporting-pipelines/commit/88ea661f80a59175cfa9a6045050f55ba8592e62))

- **deps**: Bump github/gh-aw-actions/setup from 0.74.8 to 1.4.0
  ([#179](https://github.com/michaelconan/personal-reporting-pipelines/pull/179),
  [`da973bf`](https://github.com/michaelconan/personal-reporting-pipelines/commit/da973bfd66b820c6388d03cca856a7c3fa3a2003))

- **deps**: Bump gitpython 3.1.50→3.1.54, marimo 0.23.13→0.23.15 [security]
  ([`261dde7`](https://github.com/michaelconan/personal-reporting-pipelines/commit/261dde7834af11faf55de70fe57eb3ec98d3b325))

- **deps**: Bump gitpython in the uv group across 1 directory
  ([#138](https://github.com/michaelconan/personal-reporting-pipelines/pull/138),
  [`fae6169`](https://github.com/michaelconan/personal-reporting-pipelines/commit/fae6169239b43829de6f6caddc0061642e52fd95))

- **deps**: Bump jdx/mise-action from 4.3.0 to 5.3.0
  ([#180](https://github.com/michaelconan/personal-reporting-pipelines/pull/180),
  [`ca22201`](https://github.com/michaelconan/personal-reporting-pipelines/commit/ca222015a5c9660d8c7ecae11975aa5d479621a7))

- **deps**: Bump oauthlib
  ([#152](https://github.com/michaelconan/personal-reporting-pipelines/pull/152),
  [`ef9c5ec`](https://github.com/michaelconan/personal-reporting-pipelines/commit/ef9c5ec61b04a6d1cf80d9a0f977e89e7514e7de))

- **deps**: Bump orjson in the pip group across 1 directory
  ([`aeca935`](https://github.com/michaelconan/personal-reporting-pipelines/commit/aeca93530d2d743a4438a81502cd9c6232c40e6b))

- **deps**: Bump protobuf in the pip group across 1 directory
  ([`8d09fce`](https://github.com/michaelconan/personal-reporting-pipelines/commit/8d09fcedd29be6dfe2727839f604e223190cd641))

- **deps**: Bump pymdown-extensions 10.21.3→11.0, marimo 0.23.15→0.23.16
  ([`1b00b3f`](https://github.com/michaelconan/personal-reporting-pipelines/commit/1b00b3fb4a969a3464aa23980a5e0397fc29e2c2))

- **deps**: Bump requests in the pip group across 1 directory
  ([`e0be1b0`](https://github.com/michaelconan/personal-reporting-pipelines/commit/e0be1b01c2ae8b4037f0d4de53d63bd1ae37ffae))

- **deps**: Bump the pip group across 1 directory with 2 updates
  ([`9e9b990`](https://github.com/michaelconan/personal-reporting-pipelines/commit/9e9b99065b26fad5718d266d3b7e0a11865b0e40))

- **deps**: Bump the pip group across 1 directory with 2 updates
  ([`0bd6e87`](https://github.com/michaelconan/personal-reporting-pipelines/commit/0bd6e874b3ade4c09ddd99187bf6825c18bcd8b3))

- **deps**: Bump the pip group across 1 directory with 2 updates
  ([`3027286`](https://github.com/michaelconan/personal-reporting-pipelines/commit/3027286c3dc360e4339ded56b84a41ba005d7789))

- **deps**: Bump the pip group across 1 directory with 3 updates
  ([#120](https://github.com/michaelconan/personal-reporting-pipelines/pull/120),
  [`0e3cd75`](https://github.com/michaelconan/personal-reporting-pipelines/commit/0e3cd753531609dae60a0649de162e3840f30aa7))

- **deps**: Bump the pip group across 1 directory with 3 updates
  ([#117](https://github.com/michaelconan/personal-reporting-pipelines/pull/117),
  [`bd31a00`](https://github.com/michaelconan/personal-reporting-pipelines/commit/bd31a00eb73d6b33953f5e2f71866806dfdef114))

- **deps**: Bump the pip group across 1 directory with 3 updates
  ([#120](https://github.com/michaelconan/personal-reporting-pipelines/pull/120),
  [`ce6142a`](https://github.com/michaelconan/personal-reporting-pipelines/commit/ce6142a1036be8e51fc6df8810b5d02516ff00c9))

- **deps**: Bump the pip group across 1 directory with 3 updates
  ([#119](https://github.com/michaelconan/personal-reporting-pipelines/pull/119),
  [`b0af255`](https://github.com/michaelconan/personal-reporting-pipelines/commit/b0af2552d437358ba916c0ede291c9e670801f92))

- **deps**: Bump the pip group across 1 directory with 3 updates
  ([#117](https://github.com/michaelconan/personal-reporting-pipelines/pull/117),
  [`ebaac51`](https://github.com/michaelconan/personal-reporting-pipelines/commit/ebaac511137cbe1a6e2a47138623873986fb6bba))

- **deps**: Bump the pip group across 1 directory with 3 updates
  ([`4caec0a`](https://github.com/michaelconan/personal-reporting-pipelines/commit/4caec0ae2bae4094039df416eb5b02e38e347300))

- **deps**: Bump the pip group across 1 directory with 3 updates
  ([`712bb80`](https://github.com/michaelconan/personal-reporting-pipelines/commit/712bb802a8b2b4aac6b58e9610749ceca8ead257))

- **deps**: Bump the pip group across 1 directory with 4 updates
  ([#113](https://github.com/michaelconan/personal-reporting-pipelines/pull/113),
  [`399810a`](https://github.com/michaelconan/personal-reporting-pipelines/commit/399810aa3f139bd4175cfe0c3e83f4f2653e421d))

- **deps**: Bump the pip group across 1 directory with 4 updates
  ([`fd3d7a0`](https://github.com/michaelconan/personal-reporting-pipelines/commit/fd3d7a0d47996ff50d6cc846bd0ff743ba7bb58d))

- **deps**: Bump the pip group across 1 directory with 4 updates
  ([`1ad0672`](https://github.com/michaelconan/personal-reporting-pipelines/commit/1ad0672f24813b915262481f53c649adbd784b2f))

- **deps**: Bump the pip group across 1 directory with 4 updates
  ([`315a880`](https://github.com/michaelconan/personal-reporting-pipelines/commit/315a88099a227a72c4bd05844279b98ef0947a59))

- **deps**: Bump the pip group across 1 directory with 5 updates
  ([`edc892d`](https://github.com/michaelconan/personal-reporting-pipelines/commit/edc892d12eace13c2f88f2249bf31fda982c4d78))

- **deps**: Bump the pip group across 1 directory with 5 updates
  ([`ad41d51`](https://github.com/michaelconan/personal-reporting-pipelines/commit/ad41d514d87707a75d8a938860d42b502a065278))

- **deps**: Bump the uv group across 1 directory with 2 updates
  ([#164](https://github.com/michaelconan/personal-reporting-pipelines/pull/164),
  [`cf3a2c6`](https://github.com/michaelconan/personal-reporting-pipelines/commit/cf3a2c68fa1cbf89a25589534ca575142b1f0f6b))

- **deps**: Bump the uv group across 1 directory with 2 updates
  ([#161](https://github.com/michaelconan/personal-reporting-pipelines/pull/161),
  [`5c82400`](https://github.com/michaelconan/personal-reporting-pipelines/commit/5c82400e52b40021307731fda2e05e4549764086))

- **deps**: Bump the uv group across 1 directory with 2 updates
  ([#159](https://github.com/michaelconan/personal-reporting-pipelines/pull/159),
  [`1a72384`](https://github.com/michaelconan/personal-reporting-pipelines/commit/1a72384ebc6acaddec30241107b254798d48fc71))

- **deps**: Bump the uv group across 1 directory with 2 updates
  ([`08d7d21`](https://github.com/michaelconan/personal-reporting-pipelines/commit/08d7d21c482c978ea61bb12dbffce10407bd67ca))

- **deps**: Bump the uv group across 1 directory with 3 updates
  ([#132](https://github.com/michaelconan/personal-reporting-pipelines/pull/132),
  [`a6ba035`](https://github.com/michaelconan/personal-reporting-pipelines/commit/a6ba03589e098b9ef72117250cc5232c0307f6f7))

- **deps**: Bump urllib3 in the pip group across 1 directory
  ([#82](https://github.com/michaelconan/personal-reporting-pipelines/pull/82),
  [`b5ba2f8`](https://github.com/michaelconan/personal-reporting-pipelines/commit/b5ba2f88d55f602b22ea044fe2864993bb2681cc))

- **deps-dev**: Bump filelock in the pip group across 1 directory
  ([#85](https://github.com/michaelconan/personal-reporting-pipelines/pull/85),
  [`eade96f`](https://github.com/michaelconan/personal-reporting-pipelines/commit/eade96f7cc025ced376e7e83fc71e482f730991e))

- **deps-dev**: Bump marimo in the pip group across 1 directory
  ([`0e6b8e5`](https://github.com/michaelconan/personal-reporting-pipelines/commit/0e6b8e59237db3459b5a56535b59b8e92955c333))

- **deps-dev**: Bump starlette in the pip group across 1 directory
  ([#80](https://github.com/michaelconan/personal-reporting-pipelines/pull/80),
  [`d711eeb`](https://github.com/michaelconan/personal-reporting-pipelines/commit/d711eeb370918de1d47087c33caf5dfd9be2e14b))

- **make**: Fix incorrect syntax
  ([`8d43235`](https://github.com/michaelconan/personal-reporting-pipelines/commit/8d432355c7e5d363dce0739793a06e2a9355c269))

### Continuous Integration

- Fix test workflow working directory for dbt mock target
  ([#146](https://github.com/michaelconan/personal-reporting-pipelines/pull/146),
  [`f9fede0`](https://github.com/michaelconan/personal-reporting-pipelines/commit/f9fede0c964c71a5e8dfe7ef6a441dd42ad92c4f))

- Migrate CI workflows to 1Password secrets and skip dependabot
  ([`52ab739`](https://github.com/michaelconan/personal-reporting-pipelines/commit/52ab739fd77a3170f181c1eb8bd3be311fb9fb88))

- Run mock build with steps in gap detection
  ([#169](https://github.com/michaelconan/personal-reporting-pipelines/pull/169),
  [`85e5850`](https://github.com/michaelconan/personal-reporting-pipelines/commit/85e58501c3bb503ede5d7a9793d4dee9217c8680))

- **mise**: Enable databricks-cli by registry name in workflows
  ([#151](https://github.com/michaelconan/personal-reporting-pipelines/pull/151),
  [`94e7e4d`](https://github.com/michaelconan/personal-reporting-pipelines/commit/94e7e4d7dea0628a86eba9541c69832dbee32d00))

### Documentation

- Align CI schedules and Databricks credential guidance
  ([#162](https://github.com/michaelconan/personal-reporting-pipelines/pull/162),
  [`6dd85a2`](https://github.com/michaelconan/personal-reporting-pipelines/commit/6dd85a211670a5ca3fc4b35a3506766da81b67c5))

- Consolidate Gemini context into AGENTS.md
  ([`7705547`](https://github.com/michaelconan/personal-reporting-pipelines/commit/77055471639e8b5a64efae255eb50fa4013c586c))

- Datamart status line no longer says specification/no code changes
  ([#169](https://github.com/michaelconan/personal-reporting-pipelines/pull/169),
  [`85e5850`](https://github.com/michaelconan/personal-reporting-pipelines/commit/85e58501c3bb503ede5d7a9793d4dee9217c8680))

- Fix dbt subpage configuration
  ([#79](https://github.com/michaelconan/personal-reporting-pipelines/pull/79),
  [`c624533`](https://github.com/michaelconan/personal-reporting-pipelines/commit/c62453352e8dd47580bb5f5e576d0914322c9a30))

- Fix dbt subpage configuration
  ([#76](https://github.com/michaelconan/personal-reporting-pipelines/pull/76),
  [`ea2be76`](https://github.com/michaelconan/personal-reporting-pipelines/commit/ea2be765482ce411e6ddc980ca58146a4de22e60))

- Replace workflow-specific blurb with gh-aw setup steps
  ([#116](https://github.com/michaelconan/personal-reporting-pipelines/pull/116),
  [`708875d`](https://github.com/michaelconan/personal-reporting-pipelines/commit/708875d0408dca1173af0fdb7dd9aace031b81d9))

- Update project docs for Databricks primary target and 1Password secrets
  ([`0e15f5a`](https://github.com/michaelconan/personal-reporting-pipelines/commit/0e15f5af630d8794de28a653a543d4da39d2b7e2))

- Update readme diagram
  ([`6c0d4df`](https://github.com/michaelconan/personal-reporting-pipelines/commit/6c0d4df9076d42db234bc17d83a650741a52f0eb))

- **agentcontainer**: Describe agent container setup for agentic coding
  ([#148](https://github.com/michaelconan/personal-reporting-pipelines/pull/148),
  [`80001b2`](https://github.com/michaelconan/personal-reporting-pipelines/commit/80001b2993e188ec6be384911b7b0413e873d774))

- **agents**: Document required co-author attribution
  ([#158](https://github.com/michaelconan/personal-reporting-pipelines/pull/158),
  [`88ea661`](https://github.com/michaelconan/personal-reporting-pipelines/commit/88ea661f80a59175cfa9a6045050f55ba8592e62))

- **datamart**: Add personal_progress star-schema spec
  ([#144](https://github.com/michaelconan/personal-reporting-pipelines/pull/144),
  [`35c2734`](https://github.com/michaelconan/personal-reporting-pipelines/commit/35c273413a8a726a82ef31de7dc33f120860dce5))

- **sphinx**: Expand docs — add pages for dlt, dbt layers, seeds/macros, testing & CI, gh-aw,
  architecture ([#127](https://github.com/michaelconan/personal-reporting-pipelines/pull/127),
  [`6dc6023`](https://github.com/michaelconan/personal-reporting-pipelines/commit/6dc6023b49bc24610a33826cbe7480f8d4ecd4d6))

- **sphinx**: Expand docs — add pages for dlt, dbt layers, seeds/macros, testing & CI, gh-aw,
  architecture
  ([`eca082a`](https://github.com/michaelconan/personal-reporting-pipelines/commit/eca082a1d492ebfe5031a9bc9d2fe481b43128d7))

### Features

- Add 1password secret store support
  ([`2b3ed89`](https://github.com/michaelconan/personal-reporting-pipelines/commit/2b3ed89bfbaba7739a25c13dcc75c053e8e633a2))

- Add adapter-aware dbt macros for safe casting, timestamp parsing, and date truncation with
  corresponding documentation.
  ([#88](https://github.com/michaelconan/personal-reporting-pipelines/pull/88),
  [`a478ae8`](https://github.com/michaelconan/personal-reporting-pipelines/commit/a478ae8288d0e9ab67702da564fcde029e3fe0aa))

- Add adapter-aware dbt macros for safe casting, timestamp parsing, and date truncation with
  corresponding documentation.
  ([#86](https://github.com/michaelconan/personal-reporting-pipelines/pull/86),
  [`ff61b0c`](https://github.com/michaelconan/personal-reporting-pipelines/commit/ff61b0c3d00518e41403673b56d3eee353b50ab4))

- Add adapter-aware dbt macros for safe casting, timestamp parsing, and date truncation with
  corresponding documentation.
  ([#84](https://github.com/michaelconan/personal-reporting-pipelines/pull/84),
  [`df2e77a`](https://github.com/michaelconan/personal-reporting-pipelines/commit/df2e77a49307ba18f72581a87ca3389960aff436))

- Add adapter-aware dbt macros for safe casting, timestamp parsing, and date truncation with
  corresponding documentation.
  ([#81](https://github.com/michaelconan/personal-reporting-pipelines/pull/81),
  [`9764d0a`](https://github.com/michaelconan/personal-reporting-pipelines/commit/9764d0a2e84cb516195ae0d89eb54eda3326b08f))

- Add adapter-aware dbt macros for safe casting, timestamp parsing, and date truncation with
  corresponding documentation.
  ([`da55ab3`](https://github.com/michaelconan/personal-reporting-pipelines/commit/da55ab3ab74cb529fa442061d637b9083e9f01c6))

- Add airflow configs, scripts, CI workflow, notion flows@
  ([`ae5e87e`](https://github.com/michaelconan/personal-reporting-pipelines/commit/ae5e87e33469fd3a826411e4c3807fbb41187507))

- Add azure ssh config
  ([`505c138`](https://github.com/michaelconan/personal-reporting-pipelines/commit/505c138f1e38aa0885ea80abda702e6aa4616e17))

- Add config file, script adjustments, compose variables
  ([`f18a625`](https://github.com/michaelconan/personal-reporting-pipelines/commit/f18a6252a43d977061c4828c162c4c95e25e3449))

- Add dbt project configuration and update dbt coverage commands to filter by models.
  ([#88](https://github.com/michaelconan/personal-reporting-pipelines/pull/88),
  [`a478ae8`](https://github.com/michaelconan/personal-reporting-pipelines/commit/a478ae8288d0e9ab67702da564fcde029e3fe0aa))

- Add dbt project configuration and update dbt coverage commands to filter by models.
  ([#86](https://github.com/michaelconan/personal-reporting-pipelines/pull/86),
  [`ff61b0c`](https://github.com/michaelconan/personal-reporting-pipelines/commit/ff61b0c3d00518e41403673b56d3eee353b50ab4))

- Add dbt project configuration and update dbt coverage commands to filter by models.
  ([#84](https://github.com/michaelconan/personal-reporting-pipelines/pull/84),
  [`df2e77a`](https://github.com/michaelconan/personal-reporting-pipelines/commit/df2e77a49307ba18f72581a87ca3389960aff436))

- Add dbt project configuration and update dbt coverage commands to filter by models.
  ([#81](https://github.com/michaelconan/personal-reporting-pipelines/pull/81),
  [`9764d0a`](https://github.com/michaelconan/personal-reporting-pipelines/commit/9764d0a2e84cb516195ae0d89eb54eda3326b08f))

- Add dbt project configuration and update dbt coverage commands to filter by models.
  ([`fbc40e2`](https://github.com/michaelconan/personal-reporting-pipelines/commit/fbc40e2b730a833018031367f7c2ecfb755cb58c))

- Add first dag and test configurations
  ([`214c145`](https://github.com/michaelconan/personal-reporting-pipelines/commit/214c1457ae80ac33adb2288169fedbc9a52517df))

- Add fitbit dag, update dbt models and apply sqlfluff
  ([`c3a2687`](https://github.com/michaelconan/personal-reporting-pipelines/commit/c3a26872b1548c8d9d4bd18a31c09e9646f40adc))

- Add google compute engine scripts
  ([`e24571b`](https://github.com/michaelconan/personal-reporting-pipelines/commit/e24571bffcba9376b2bd37c9a99b3a133f817a6b))

- Add honcho Procfile, airflow config, startup command
  ([`caf4b3c`](https://github.com/michaelconan/personal-reporting-pipelines/commit/caf4b3cfb6b089708ba73ccd91e68ca981a0fc16))

- Add hubspot tables and dags, monthly notion tables
  ([`bdc4132`](https://github.com/michaelconan/personal-reporting-pipelines/commit/bdc4132c38bd1e6fc4d93817e786f925c7c572e3))

- Add initial airflow setup, containers and notes
  ([`e477a40`](https://github.com/michaelconan/personal-reporting-pipelines/commit/e477a40fac08a95739708ac739eee3ad0f599ac6))

- Add initial dbt model, update notion tests
  ([`c2f5bb9`](https://github.com/michaelconan/personal-reporting-pipelines/commit/c2f5bb9187cd26dd5cc7751270e035fab9d2ae12))

- Add macros to simplify models
  ([#88](https://github.com/michaelconan/personal-reporting-pipelines/pull/88),
  [`a478ae8`](https://github.com/michaelconan/personal-reporting-pipelines/commit/a478ae8288d0e9ab67702da564fcde029e3fe0aa))

- Add macros to simplify models
  ([#86](https://github.com/michaelconan/personal-reporting-pipelines/pull/86),
  [`ff61b0c`](https://github.com/michaelconan/personal-reporting-pipelines/commit/ff61b0c3d00518e41403673b56d3eee353b50ab4))

- Add macros to simplify models
  ([#84](https://github.com/michaelconan/personal-reporting-pipelines/pull/84),
  [`df2e77a`](https://github.com/michaelconan/personal-reporting-pipelines/commit/df2e77a49307ba18f72581a87ca3389960aff436))

- Add macros to simplify models
  ([#81](https://github.com/michaelconan/personal-reporting-pipelines/pull/81),
  [`9764d0a`](https://github.com/michaelconan/personal-reporting-pipelines/commit/9764d0a2e84cb516195ae0d89eb54eda3326b08f))

- Add macros to simplify models
  ([`007e93f`](https://github.com/michaelconan/personal-reporting-pipelines/commit/007e93f817f19a72e729011cb520ce7aac08a01d))

- Add Marimo to Pipfile for interactive data exploration.
  ([`f8e7e03`](https://github.com/michaelconan/personal-reporting-pipelines/commit/f8e7e030e44a9cd07e50c7461a3fab3a7e9850b6))

- Add migrations, raw notion load, dbt config
  ([`8f9dece`](https://github.com/michaelconan/personal-reporting-pipelines/commit/8f9dece7470462ee16bd149599e4315b8ad71104))

- Add monthly delete reconciliation workflow
  ([#172](https://github.com/michaelconan/personal-reporting-pipelines/pull/172),
  [`48afdff`](https://github.com/michaelconan/personal-reporting-pipelines/commit/48afdff3889c9fd255b2d8599e57e31c5e40581c))

- Add refresh targets for Fitbit, Notion, and HubSpot pipelines; implement secret validation
  ([`0d71c10`](https://github.com/michaelconan/personal-reporting-pipelines/commit/0d71c107810d1c2ba5c765ff9e7849886fd7bd45))

- Add stg_ prefix to notion model
  ([`18889e4`](https://github.com/michaelconan/personal-reporting-pipelines/commit/18889e42c1f3bd00a64679b62b426ee40a76ec6c))

- Add unpivoted habits model and associated properties for tracking daily, weekly, and monthly
  habits ([#88](https://github.com/michaelconan/personal-reporting-pipelines/pull/88),
  [`a478ae8`](https://github.com/michaelconan/personal-reporting-pipelines/commit/a478ae8288d0e9ab67702da564fcde029e3fe0aa))

- Add unpivoted habits model and associated properties for tracking daily, weekly, and monthly
  habits ([#86](https://github.com/michaelconan/personal-reporting-pipelines/pull/86),
  [`ff61b0c`](https://github.com/michaelconan/personal-reporting-pipelines/commit/ff61b0c3d00518e41403673b56d3eee353b50ab4))

- Add unpivoted habits model and associated properties for tracking daily, weekly, and monthly
  habits ([#84](https://github.com/michaelconan/personal-reporting-pipelines/pull/84),
  [`df2e77a`](https://github.com/michaelconan/personal-reporting-pipelines/commit/df2e77a49307ba18f72581a87ca3389960aff436))

- Add unpivoted habits model and associated properties for tracking daily, weekly, and monthly
  habits ([#81](https://github.com/michaelconan/personal-reporting-pipelines/pull/81),
  [`9764d0a`](https://github.com/michaelconan/personal-reporting-pipelines/commit/9764d0a2e84cb516195ae0d89eb54eda3326b08f))

- Add unpivoted habits model and associated properties for tracking daily, weekly, and monthly
  habits
  ([`847b387`](https://github.com/michaelconan/personal-reporting-pipelines/commit/847b387ad7ab121cc8cc98a4b688c66a44228477))

- Add unpivoted habits model and associated properties for tracki…
  ([#81](https://github.com/michaelconan/personal-reporting-pipelines/pull/81),
  [`9764d0a`](https://github.com/michaelconan/personal-reporting-pipelines/commit/9764d0a2e84cb516195ae0d89eb54eda3326b08f))

- Add weekly Monday morning documentation updater workflow
  ([`ab04aec`](https://github.com/michaelconan/personal-reporting-pipelines/commit/ab04aecf5a61450807e164f81c9c4011a3f07eb9))

- Add WIP version of fitbit DAG, other edits
  ([`47801ec`](https://github.com/michaelconan/personal-reporting-pipelines/commit/47801ec755f4016c1c20034c40d3da46d184c952))

- Capture deleted HubSpot records via archived sweep
  ([#172](https://github.com/michaelconan/personal-reporting-pipelines/pull/172),
  [`48afdff`](https://github.com/michaelconan/personal-reporting-pipelines/commit/48afdff3889c9fd255b2d8599e57e31c5e40581c))

- Capture deleted HubSpot records via archived sweep (#43)
  ([#172](https://github.com/michaelconan/personal-reporting-pipelines/pull/172),
  [`48afdff`](https://github.com/michaelconan/personal-reporting-pipelines/commit/48afdff3889c9fd255b2d8599e57e31c5e40581c))

- Comprehensive dbt model updates and pipeline improvements
  ([#146](https://github.com/michaelconan/personal-reporting-pipelines/pull/146),
  [`f9fede0`](https://github.com/michaelconan/personal-reporting-pipelines/commit/f9fede0c964c71a5e8dfe7ef6a441dd42ad92c4f))

- Convert from docker to standard python app
  ([`a331423`](https://github.com/michaelconan/personal-reporting-pipelines/commit/a331423604ece88397e417c429252b810501cdd7))

- Default to MotherDuck (dev-md/test-md/prod-md)
  ([`2c45b59`](https://github.com/michaelconan/personal-reporting-pipelines/commit/2c45b595eea5b3dcd7c7e7c290b09f2e2fd21181))

- Enhance CI workflows and add code coverage reporting
  ([`b218825`](https://github.com/michaelconan/personal-reporting-pipelines/commit/b218825bcec294af47bf10b5bb188e04f95e9696))

- Enhance dbt mock configuration and dlt pipeline execution cli mechanism
  ([#127](https://github.com/michaelconan/personal-reporting-pipelines/pull/127),
  [`6dc6023`](https://github.com/michaelconan/personal-reporting-pipelines/commit/6dc6023b49bc24610a33826cbe7480f8d4ecd4d6))

- Enhance dbt mock configuration and dlt pipeline execution cli mechanism
  ([`670e2fa`](https://github.com/michaelconan/personal-reporting-pipelines/commit/670e2fa5ef84314b57801aa46bd141f028bbba63))

- Enhance dbt models and workflows with new data tests and Makefile updates
  ([`7b02727`](https://github.com/michaelconan/personal-reporting-pipelines/commit/7b0272720ae1e80a9ed19ea3a3fec378c5cfb9fb))

- Enhance dbt models with cross-database support and improved testing
  ([#79](https://github.com/michaelconan/personal-reporting-pipelines/pull/79),
  [`c624533`](https://github.com/michaelconan/personal-reporting-pipelines/commit/c62453352e8dd47580bb5f5e576d0914322c9a30))

- Enhance documentation and project configuration
  ([#79](https://github.com/michaelconan/personal-reporting-pipelines/pull/79),
  [`c624533`](https://github.com/michaelconan/personal-reporting-pipelines/commit/c62453352e8dd47580bb5f5e576d0914322c9a30))

- Enhance documentation and project configuration
  ([#76](https://github.com/michaelconan/personal-reporting-pipelines/pull/76),
  [`ea2be76`](https://github.com/michaelconan/personal-reporting-pipelines/commit/ea2be765482ce411e6ddc980ca58146a4de22e60))

- Enhance documentation and project configuration
  ([#75](https://github.com/michaelconan/personal-reporting-pipelines/pull/75),
  [`a72ce18`](https://github.com/michaelconan/personal-reporting-pipelines/commit/a72ce18984fe19c2e72d584f69ce713c1f4b26d0))

- Enhance documentation and project configuration
  ([#74](https://github.com/michaelconan/personal-reporting-pipelines/pull/74),
  [`9595a6f`](https://github.com/michaelconan/personal-reporting-pipelines/commit/9595a6f1e4ffb1d912ecab3a4bbf09d35fc38fc0))

- Enhance Makefile and README for dbt project management
  ([`3a5af94`](https://github.com/michaelconan/personal-reporting-pipelines/commit/3a5af949dc34425929a0399772ce229053927e67))

- Integrate Marimo and enhance dbt development workflow
  ([`f8e7e03`](https://github.com/michaelconan/personal-reporting-pipelines/commit/f8e7e030e44a9cd07e50c7461a3fab3a7e9850b6))

- Migrate dbt models to new API data model and add discipline metrics
  ([`630c84d`](https://github.com/michaelconan/personal-reporting-pipelines/commit/630c84de05218e9d20c311d69aa6855e2be0ba94))

- Migrate from Airflow to dlt with GitHub Actions orchestration
  ([`e1c6c68`](https://github.com/michaelconan/personal-reporting-pipelines/commit/e1c6c68dd0e9cd55bab4035f25db308d9bf41787))

- Migrate notion dag to use dlt
  ([`394b7db`](https://github.com/michaelconan/personal-reporting-pipelines/commit/394b7db04e6e06e83ad958494f2d1351e606d569))

- Recover mise migration and session work from stashes
  ([#151](https://github.com/michaelconan/personal-reporting-pipelines/pull/151),
  [`94e7e4d`](https://github.com/michaelconan/personal-reporting-pipelines/commit/94e7e4d7dea0628a86eba9541c69832dbee32d00))

- Refactor GitHub Actions workflows and update dbt profiles
  ([`9fe2f20`](https://github.com/michaelconan/personal-reporting-pipelines/commit/9fe2f20491757b50861e702f79d93b4d2d67e312))

- Refactor HubSpot and Notion pipelines for improved data ingestion
  ([`0b1cd4d`](https://github.com/michaelconan/personal-reporting-pipelines/commit/0b1cd4d7a1223f8e1c36ac5b913fe0256f1a62cd))

- Refactor pipelines and add comprehensive unit tests
  ([`e9cb193`](https://github.com/michaelconan/personal-reporting-pipelines/commit/e9cb193126c5d3ab01e32a2021a9d32d07d44a59))

- Refine marts, add semantic models, improve documentation
  ([#88](https://github.com/michaelconan/personal-reporting-pipelines/pull/88),
  [`a478ae8`](https://github.com/michaelconan/personal-reporting-pipelines/commit/a478ae8288d0e9ab67702da564fcde029e3fe0aa))

- Refine marts, add semantic models, improve documentation
  ([`ee0aa5f`](https://github.com/michaelconan/personal-reporting-pipelines/commit/ee0aa5f8b873b11010f04d8746060cef8edb32cf))

- Rename dbt project to match dags 'michael'
  ([`2870833`](https://github.com/michaelconan/personal-reporting-pipelines/commit/287083370004ada20afa6b264e6a1d8838917938))

- Replace Claude doc updater with GitHub Copilot coding agent
  ([#114](https://github.com/michaelconan/personal-reporting-pipelines/pull/114),
  [`5b51d50`](https://github.com/michaelconan/personal-reporting-pipelines/commit/5b51d50ae10135ed9422fed95c0995f31c9ce5fb))

- Route pipeline logs to stdout with unbuffered output
  ([#110](https://github.com/michaelconan/personal-reporting-pipelines/pull/110),
  [`0413d9e`](https://github.com/michaelconan/personal-reporting-pipelines/commit/0413d9e1c7388c308069d8005b767d0ca978a175))

- Separate alembic migrations
  ([`b5c838b`](https://github.com/michaelconan/personal-reporting-pipelines/commit/b5c838ba1dc3cce57ae28c06bead5c953fe00030))

- Simplify and reconfigure docker image, add registry workflow
  ([`ce3f2f2`](https://github.com/michaelconan/personal-reporting-pipelines/commit/ce3f2f2055e24fdd825e74dcd424276b94667a24))

- Switch weekly doc updater engine from claude to copilot
  ([#114](https://github.com/michaelconan/personal-reporting-pipelines/pull/114),
  [`5b51d50`](https://github.com/michaelconan/personal-reporting-pipelines/commit/5b51d50ae10135ed9422fed95c0995f31c9ce5fb))

- Update dag names, config, docs
  ([`d6670f7`](https://github.com/michaelconan/personal-reporting-pipelines/commit/d6670f720e83b92273a0a82eae7aba6a48745bca))

- Update data tests, add workflow to generate dbt docs for pages
  ([`671b751`](https://github.com/michaelconan/personal-reporting-pipelines/commit/671b751416429153fbd373b586b5e565a20f9c50))

- Update datasets for DBT scheduling
  ([`fa262b4`](https://github.com/michaelconan/personal-reporting-pipelines/commit/fa262b48c8b74a22dbbe39abd3415be7e82fbc0e))

- Update dbt hubspot models and add data tests
  ([`799732a`](https://github.com/michaelconan/personal-reporting-pipelines/commit/799732acb270a71fc2e1672e98a2600f7fc82160))

- Update dbt models to dlt schema
  ([`1da27ee`](https://github.com/michaelconan/personal-reporting-pipelines/commit/1da27eef66f12e8351b2fcae0eb081fdb16d75c6))

- Update dbt models to dlt schema
  ([`1d2450e`](https://github.com/michaelconan/personal-reporting-pipelines/commit/1d2450e39d45621e6854929e1c3314d223c88c73))

- Update dev container config, naming, run pre commit
  ([`5d5f738`](https://github.com/michaelconan/personal-reporting-pipelines/commit/5d5f738956227cfe80a899f0774209bdd6be60c2))

- Update docker for SSH, action to publish to web app
  ([`908dd1f`](https://github.com/michaelconan/personal-reporting-pipelines/commit/908dd1fae11f315d20ce2df2ccf9b44b7cd03a74))

- Update downgrade drop statements with schemas and if exists
  ([`9c21f14`](https://github.com/michaelconan/personal-reporting-pipelines/commit/9c21f14d2bd281e4cae3ac5e3688f0fabc36ce1f))

- Update hubspot dags and related dbt models
  ([`863deb1`](https://github.com/michaelconan/personal-reporting-pipelines/commit/863deb1b5e77ae2c0d18e3065ffeb12f9086f429))

- Update hubspot dags to dlt
  ([`2b19534`](https://github.com/michaelconan/personal-reporting-pipelines/commit/2b195344a2ed08c2244c3eb0922e211ffff2b361))

- Update migrations, loading dags, dbt config and tests
  ([`120cebd`](https://github.com/michaelconan/personal-reporting-pipelines/commit/120cebdb8b22b73eabf47b4f6ea9c4506f074069))

- Update notion and hubspot dlt dags, remove alembic
  ([`859aa34`](https://github.com/michaelconan/personal-reporting-pipelines/commit/859aa34f060f0073f85a06fef5a3bae8a03bce2a))

- Update schema loading, dbt models
  ([`b928955`](https://github.com/michaelconan/personal-reporting-pipelines/commit/b928955f12fabcdeeb109527a9d578a6c4c7e24c))

- Update security and configs
  ([`5a2773a`](https://github.com/michaelconan/personal-reporting-pipelines/commit/5a2773aecea22d8ad05c803fe155de94b33111d2))

- Weekly Monday morning documentation updater workflow
  ([#112](https://github.com/michaelconan/personal-reporting-pipelines/pull/112),
  [`5a8a15c`](https://github.com/michaelconan/personal-reporting-pipelines/commit/5a8a15ca9f6115deea515596600c38fe0250b363))

- **agentcontainer**: Add GitHub CLI and fix entrypoint git config
  ([`d605e04`](https://github.com/michaelconan/personal-reporting-pipelines/commit/d605e04ef51c3b4a3cc58a60e8b475dbd09bbf65))

- **agentcontainer**: Docker secrets and user config mounts
  ([`f60e841`](https://github.com/michaelconan/personal-reporting-pipelines/commit/f60e84165d2abea5b018649cbedc44e9f21ce077))

- **agentcontainer**: Update Docker secrets, compose config, and entrypoint
  ([`9a9b703`](https://github.com/michaelconan/personal-reporting-pipelines/commit/9a9b703519246333989ec8ac4fd4f378f5dfcb6f))

- **dbt**: Add core layer and replace fitbit with google health
  ([#144](https://github.com/michaelconan/personal-reporting-pipelines/pull/144),
  [`35c2734`](https://github.com/michaelconan/personal-reporting-pipelines/commit/35c273413a8a726a82ef31de7dc33f120860dce5))

- **dbt**: Add core layer and replace fitbit with google health
  ([#140](https://github.com/michaelconan/personal-reporting-pipelines/pull/140),
  [`23acc0f`](https://github.com/michaelconan/personal-reporting-pipelines/commit/23acc0f3e90a0ad2bebca0e626450bebfe504963))

- **dbt**: Add Databricks Unity Catalog as primary target
  ([`489129c`](https://github.com/michaelconan/personal-reporting-pipelines/commit/489129c378d1df218e85c1a92cb08572b2961d5a))

- **dbt**: Add fct_health_data_gaps mart with steps toggle
  ([#169](https://github.com/michaelconan/personal-reporting-pipelines/pull/169),
  [`85e5850`](https://github.com/michaelconan/personal-reporting-pipelines/commit/85e58501c3bb503ede5d7a9793d4dee9217c8680))

- **dbt**: Add fct_health_data_gaps mart with steps toggle (#134)
  ([#169](https://github.com/michaelconan/personal-reporting-pipelines/pull/169),
  [`85e5850`](https://github.com/michaelconan/personal-reporting-pipelines/commit/85e58501c3bb503ede5d7a9793d4dee9217c8680))

- **dbt**: Add personal_progress datamart marts
  ([#144](https://github.com/michaelconan/personal-reporting-pipelines/pull/144),
  [`35c2734`](https://github.com/michaelconan/personal-reporting-pipelines/commit/35c273413a8a726a82ef31de7dc33f120860dce5))

- **dbt**: Dbt 2.x upgrade, source freshness, static docs, and personal_progress datamart
  ([#144](https://github.com/michaelconan/personal-reporting-pipelines/pull/144),
  [`35c2734`](https://github.com/michaelconan/personal-reporting-pipelines/commit/35c273413a8a726a82ef31de7dc33f120860dce5))

- **dbt**: Enforce governance checks and recommended model structure
  ([#144](https://github.com/michaelconan/personal-reporting-pipelines/pull/144),
  [`35c2734`](https://github.com/michaelconan/personal-reporting-pipelines/commit/35c273413a8a726a82ef31de7dc33f120860dce5))

- **dbt**: Enforce governance checks and recommended model structure
  ([#140](https://github.com/michaelconan/personal-reporting-pipelines/pull/140),
  [`23acc0f`](https://github.com/michaelconan/personal-reporting-pipelines/commit/23acc0f3e90a0ad2bebca0e626450bebfe504963))

- **dbt**: Move not_null to constraints and enforce primary keys
  ([#144](https://github.com/michaelconan/personal-reporting-pipelines/pull/144),
  [`35c2734`](https://github.com/michaelconan/personal-reporting-pipelines/commit/35c273413a8a726a82ef31de7dc33f120860dce5))

- **dbt**: Move not_null to constraints and enforce primary keys
  ([#140](https://github.com/michaelconan/personal-reporting-pipelines/pull/140),
  [`23acc0f`](https://github.com/michaelconan/personal-reporting-pipelines/commit/23acc0f3e90a0ad2bebca0e626450bebfe504963))

- **dbt**: Organise macros, upate docs, format yml
  ([#144](https://github.com/michaelconan/personal-reporting-pipelines/pull/144),
  [`35c2734`](https://github.com/michaelconan/personal-reporting-pipelines/commit/35c273413a8a726a82ef31de7dc33f120860dce5))

- **dbt**: Organise macros, upate docs, format yml
  ([#140](https://github.com/michaelconan/personal-reporting-pipelines/pull/140),
  [`23acc0f`](https://github.com/michaelconan/personal-reporting-pipelines/commit/23acc0f3e90a0ad2bebca0e626450bebfe504963))

- **dlt**: Repoint ingestion destination to Databricks direct load
  ([#146](https://github.com/michaelconan/personal-reporting-pipelines/pull/146),
  [`f9fede0`](https://github.com/michaelconan/personal-reporting-pipelines/commit/f9fede0c964c71a5e8dfe7ef6a441dd42ad92c4f))

- **google-health**: Add token refresh using google-auth, unit tests and mock data
  ([`a9beecd`](https://github.com/michaelconan/personal-reporting-pipelines/commit/a9beecd2ca5d5ad015d82c26e90354bdddc8a199))

- **google-health**: Filter exercise data points server-side
  ([#158](https://github.com/michaelconan/personal-reporting-pipelines/pull/158),
  [`88ea661`](https://github.com/michaelconan/personal-reporting-pipelines/commit/88ea661f80a59175cfa9a6045050f55ba8592e62))

- **google-health**: Refactor GitHub workflows and add Google Health pipeline
  ([`4a0256a`](https://github.com/michaelconan/personal-reporting-pipelines/commit/4a0256a39a4036408cae86fe36fcaf1d525c6e95))

- **mise**: Replace Makefile workflows with direct tasks
  ([#151](https://github.com/michaelconan/personal-reporting-pipelines/pull/151),
  [`94e7e4d`](https://github.com/michaelconan/personal-reporting-pipelines/commit/94e7e4d7dea0628a86eba9541c69832dbee32d00))

- **mocks**: Update mock response data generation script for unit tests
  ([#139](https://github.com/michaelconan/personal-reporting-pipelines/pull/139),
  [`4c37c6f`](https://github.com/michaelconan/personal-reporting-pipelines/commit/4c37c6f89c1583682dd5818ac2b045070d9cb020))

- **scripts**: Add mock API response generator and modularize data scrubbing
  ([`78f7e19`](https://github.com/michaelconan/personal-reporting-pipelines/commit/78f7e195f4f31e759d080522dce716d6e6b2f598))

- **scripts**: Add mock API response generator and modularize data scrubbing
  ([#139](https://github.com/michaelconan/personal-reporting-pipelines/pull/139),
  [`4c37c6f`](https://github.com/michaelconan/personal-reporting-pipelines/commit/4c37c6f89c1583682dd5818ac2b045070d9cb020))

- **tests**: Restructure suites into unit/integration/e2e and retire Fitbit dlt
  ([#139](https://github.com/michaelconan/personal-reporting-pipelines/pull/139),
  [`4c37c6f`](https://github.com/michaelconan/personal-reporting-pipelines/commit/4c37c6f89c1583682dd5818ac2b045070d9cb020))

### Refactoring

- Improve macro patterns and documentation
  ([#79](https://github.com/michaelconan/personal-reporting-pipelines/pull/79),
  [`c624533`](https://github.com/michaelconan/personal-reporting-pipelines/commit/c62453352e8dd47580bb5f5e576d0914322c9a30))

- Replace self-join with LEAD() to detect overlapping sleep logs
  ([`fa7ae7d`](https://github.com/michaelconan/personal-reporting-pipelines/commit/fa7ae7d153caa75a8f246c8b4c12a02e051d2c52))

- Replace yml+toml with agentic md workflow for weekly doc updater
  ([`b3e2483`](https://github.com/michaelconan/personal-reporting-pipelines/commit/b3e2483afd6c58a53a0c5b6abc5bf96ac97ad3ca))

- Update dbt models and documentation
  ([`355ba87`](https://github.com/michaelconan/personal-reporting-pipelines/commit/355ba879f975e6044987e702e6dd76576a46437c))

- Use dbt_utils.deduplicate in stg_fitbit__sleep now that macro is fixed
  ([`f56d1d6`](https://github.com/michaelconan/personal-reporting-pipelines/commit/f56d1d60514463d1a999434191b98885cbc09803))

### Revert

- Restore Gemini workflows, remove copilot.yml
  ([#114](https://github.com/michaelconan/personal-reporting-pipelines/pull/114),
  [`5b51d50`](https://github.com/michaelconan/personal-reporting-pipelines/commit/5b51d50ae10135ed9422fed95c0995f31c9ce5fb))

### Testing

- Enhance HubSpot integration testing infrastructure
  ([`c8b2335`](https://github.com/michaelconan/personal-reporting-pipelines/commit/c8b23354eae4b7cf45961b642540c7dabbcc0618))

- Enhance HubSpot pipeline testing and CI infrastructure
  ([`a1a2b90`](https://github.com/michaelconan/personal-reporting-pipelines/commit/a1a2b903c1a9f146dfa08fc5e36da3466b72c177))

- Enhance test coverage and pipeline configuration
  ([`e34b680`](https://github.com/michaelconan/personal-reporting-pipelines/commit/e34b680de19be1c15378276cfdbdf5e0a168fcf0))

- Fix unit tests for HubSpot and Notion pipeline migrations
  ([`98cafe2`](https://github.com/michaelconan/personal-reporting-pipelines/commit/98cafe21dc68dd095403a6e302a4369fd18eefc2))

- Rename workflow files and improve test configuration
  ([`2706732`](https://github.com/michaelconan/personal-reporting-pipelines/commit/2706732cecf8bc3a4083dd393d847b38fdab8252))

- **dlt**: Fix HubSpot and Notion fixtures
  ([#139](https://github.com/michaelconan/personal-reporting-pipelines/pull/139),
  [`4c37c6f`](https://github.com/michaelconan/personal-reporting-pipelines/commit/4c37c6f89c1583682dd5818ac2b045070d9cb020))

- **dlt**: Fix HubSpot and Notion unit tests
  ([#139](https://github.com/michaelconan/personal-reporting-pipelines/pull/139),
  [`4c37c6f`](https://github.com/michaelconan/personal-reporting-pipelines/commit/4c37c6f89c1583682dd5818ac2b045070d9cb020))

- **google-health**: Cover civil bound date and unsupported inputs
  ([#158](https://github.com/michaelconan/personal-reporting-pipelines/pull/158),
  [`88ea661`](https://github.com/michaelconan/personal-reporting-pipelines/commit/88ea661f80a59175cfa9a6045050f55ba8592e62))

- **google-health**: Cover civil filter offset stripping
  ([#158](https://github.com/michaelconan/personal-reporting-pipelines/pull/158),
  [`88ea661`](https://github.com/michaelconan/personal-reporting-pipelines/commit/88ea661f80a59175cfa9a6045050f55ba8592e62))
