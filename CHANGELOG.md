# Changelog

## 0.10.0 (2025-03-17)

Full Changelog: [v0.9.0...v0.10.0](https://github.com/riza-io/riza-api-python/compare/v0.9.0...v0.10.0)

### Features

* **api:** api update ([#145](https://github.com/riza-io/riza-api-python/issues/145)) ([6f94e74](https://github.com/riza-io/riza-api-python/commit/6f94e74f384b9b7a4f96164fc6b65ba915f44b41))


### Bug Fixes

* **ci:** ensure pip is always available ([#151](https://github.com/riza-io/riza-api-python/issues/151)) ([4e1aaa0](https://github.com/riza-io/riza-api-python/commit/4e1aaa0804c8b90b4c65dc3d51e8ec3ac574ebbc))
* **ci:** remove publishing patch ([#152](https://github.com/riza-io/riza-api-python/issues/152)) ([fc6302b](https://github.com/riza-io/riza-api-python/commit/fc6302b096cb4d6763397075f5f6707dde0df74e))
* **types:** handle more discriminated union shapes ([#150](https://github.com/riza-io/riza-api-python/issues/150)) ([142b585](https://github.com/riza-io/riza-api-python/commit/142b58513dff2902d976dbc99171fa18b15b157f))


### Chores

* **internal:** bump rye to 0.44.0 ([#149](https://github.com/riza-io/riza-api-python/issues/149)) ([eda0bf5](https://github.com/riza-io/riza-api-python/commit/eda0bf5410ee7f84e4a584ed7c48f12512317c45))
* **internal:** codegen related update ([#148](https://github.com/riza-io/riza-api-python/issues/148)) ([3941fce](https://github.com/riza-io/riza-api-python/commit/3941fce6c6bda47dd81474afa6eb4d092ecfc1ba))
* **internal:** remove extra empty newlines ([#147](https://github.com/riza-io/riza-api-python/issues/147)) ([1b710bb](https://github.com/riza-io/riza-api-python/commit/1b710bb900191f4eec5a51565f5776c6a25b08fa))

## 0.9.0 (2025-03-11)

Full Changelog: [v0.8.0...v0.9.0](https://github.com/riza-io/riza-api-python/compare/v0.8.0...v0.9.0)

### Features

* **api:** api update ([#133](https://github.com/riza-io/riza-api-python/issues/133)) ([f3fd506](https://github.com/riza-io/riza-api-python/commit/f3fd506b53a825bfacae9346d99b36775b2eaab9))
* **api:** api update ([#136](https://github.com/riza-io/riza-api-python/issues/136)) ([9095362](https://github.com/riza-io/riza-api-python/commit/909536270fa373d63c51f28f10cc8cae1865f6da))
* **api:** api update ([#141](https://github.com/riza-io/riza-api-python/issues/141)) ([b0ff99a](https://github.com/riza-io/riza-api-python/commit/b0ff99a573bee3d4f6b7f167bdbdd4d5e73649cb))
* **client:** allow passing `NotGiven` for body ([#134](https://github.com/riza-io/riza-api-python/issues/134)) ([b5a1ab9](https://github.com/riza-io/riza-api-python/commit/b5a1ab9dbdc6981c17ebb9fd08fc45378dec0662))
* **client:** send `X-Stainless-Read-Timeout` header ([#127](https://github.com/riza-io/riza-api-python/issues/127)) ([d2629cf](https://github.com/riza-io/riza-api-python/commit/d2629cfece0ad9f4738d4b50b90334d27412b7da))


### Bug Fixes

* asyncify on non-asyncio runtimes ([#132](https://github.com/riza-io/riza-api-python/issues/132)) ([ce5e5b0](https://github.com/riza-io/riza-api-python/commit/ce5e5b0d7b854af7212cc6a34129cd0823dda109))
* **client:** mark some request bodies as optional ([b5a1ab9](https://github.com/riza-io/riza-api-python/commit/b5a1ab9dbdc6981c17ebb9fd08fc45378dec0662))


### Chores

* **docs:** update client docstring ([#139](https://github.com/riza-io/riza-api-python/issues/139)) ([f897bc5](https://github.com/riza-io/riza-api-python/commit/f897bc54e13dbbd2a09f35ebed272255f3e5ab02))
* **internal:** fix devcontainers setup ([#135](https://github.com/riza-io/riza-api-python/issues/135)) ([cc94121](https://github.com/riza-io/riza-api-python/commit/cc941211ec216cb16432fe5f9bdaf0fe64c70a31))
* **internal:** fix type traversing dictionary params ([#129](https://github.com/riza-io/riza-api-python/issues/129)) ([8cfb90d](https://github.com/riza-io/riza-api-python/commit/8cfb90d3cdd56468276a1387a20ec5653e80e758))
* **internal:** minor type handling changes ([#130](https://github.com/riza-io/riza-api-python/issues/130)) ([778f16d](https://github.com/riza-io/riza-api-python/commit/778f16d7b44115f15424b2bb6c3d7659d209d3ea))
* **internal:** properly set __pydantic_private__ ([#137](https://github.com/riza-io/riza-api-python/issues/137)) ([ad8f1bb](https://github.com/riza-io/riza-api-python/commit/ad8f1bbbec2509465d6bada2c9f69c3e0db0c51a))
* **internal:** remove unused http client options forwarding ([#140](https://github.com/riza-io/riza-api-python/issues/140)) ([91eb039](https://github.com/riza-io/riza-api-python/commit/91eb039a636d9fc2725c25fcf8d90ab9b4bf502e))
* **internal:** update client tests ([#131](https://github.com/riza-io/riza-api-python/issues/131)) ([3e9339e](https://github.com/riza-io/riza-api-python/commit/3e9339ee374e19dfe87a752046d370644df05e3b))


### Documentation

* revise readme docs about nested params ([#142](https://github.com/riza-io/riza-api-python/issues/142)) ([ad0478e](https://github.com/riza-io/riza-api-python/commit/ad0478eeb05cfb65d5abeff560b0aea74a1d5d70))
* update URLs from stainlessapi.com to stainless.com ([#138](https://github.com/riza-io/riza-api-python/issues/138)) ([b3146ea](https://github.com/riza-io/riza-api-python/commit/b3146eac22b432b11d122089635362d6f09e403f))

## 0.8.0 (2025-02-04)

Full Changelog: [v0.7.0...v0.8.0](https://github.com/riza-io/riza-api-python/compare/v0.7.0...v0.8.0)

### Features

* **api:** api update ([#115](https://github.com/riza-io/riza-api-python/issues/115)) ([26f031e](https://github.com/riza-io/riza-api-python/commit/26f031edd8df146556a48a2cec50c1c23ebd0d4e))
* **api:** api update ([#117](https://github.com/riza-io/riza-api-python/issues/117)) ([4105478](https://github.com/riza-io/riza-api-python/commit/41054787b55ec678f3389f40dd70f9edfcd7d950))
* **api:** api update ([#119](https://github.com/riza-io/riza-api-python/issues/119)) ([fa14cbf](https://github.com/riza-io/riza-api-python/commit/fa14cbf315c66627082bfef281477a574b67dbfa))
* **api:** api update ([#120](https://github.com/riza-io/riza-api-python/issues/120)) ([02d8740](https://github.com/riza-io/riza-api-python/commit/02d87408c52a8c495cc87119f89d613019665dc0))
* **api:** api update ([#121](https://github.com/riza-io/riza-api-python/issues/121)) ([e168ac4](https://github.com/riza-io/riza-api-python/commit/e168ac4cf58dc61052fd0ca721610e9004fbf22d))
* **api:** api update ([#122](https://github.com/riza-io/riza-api-python/issues/122)) ([ec346bf](https://github.com/riza-io/riza-api-python/commit/ec346bffdc56c0868c52932721e2648fc584d58b))
* **api:** api update ([#123](https://github.com/riza-io/riza-api-python/issues/123)) ([14f6367](https://github.com/riza-io/riza-api-python/commit/14f6367def814ce48910dffc22f83c24997b06f1))


### Chores

* **internal:** change default timeout to an int ([#124](https://github.com/riza-io/riza-api-python/issues/124)) ([0cc525c](https://github.com/riza-io/riza-api-python/commit/0cc525cddd1b57d169ad6af58427b4e3f8e9abbe))
* **internal:** minor formatting changes ([#118](https://github.com/riza-io/riza-api-python/issues/118)) ([61fdf26](https://github.com/riza-io/riza-api-python/commit/61fdf26af69850b576e4ea8058c6c72940217811))

## 0.7.0 (2025-01-23)

Full Changelog: [v0.6.0...v0.7.0](https://github.com/riza-io/riza-api-python/compare/v0.6.0...v0.7.0)

### Features

* **api:** api update ([#113](https://github.com/riza-io/riza-api-python/issues/113)) ([b2f6eda](https://github.com/riza-io/riza-api-python/commit/b2f6eda906a7d25e5b0e02097d214da2b4294469))


### Bug Fixes

* reuse model in pagination items type ([#111](https://github.com/riza-io/riza-api-python/issues/111)) ([6472cde](https://github.com/riza-io/riza-api-python/commit/6472cde6c7b552d557a2521959d82701227444ec))


### Chores

* **internal:** codegen related update ([#109](https://github.com/riza-io/riza-api-python/issues/109)) ([0b3e8c7](https://github.com/riza-io/riza-api-python/commit/0b3e8c7cd5d4337d412421334bb7c75b2f8ba4f3))
* **internal:** minor style changes ([#112](https://github.com/riza-io/riza-api-python/issues/112)) ([eeef003](https://github.com/riza-io/riza-api-python/commit/eeef0036501132b303398f42a17e2f5cf2a47c46))

## 0.6.0 (2025-01-16)

Full Changelog: [v0.5.0...v0.6.0](https://github.com/riza-io/riza-api-python/compare/v0.5.0...v0.6.0)

### Features

* **api:** api update ([#106](https://github.com/riza-io/riza-api-python/issues/106)) ([1cc6f50](https://github.com/riza-io/riza-api-python/commit/1cc6f500aeb590cc1523e6f072de0ebe66b8525b))

## 0.5.0 (2025-01-10)

Full Changelog: [v0.4.0...v0.5.0](https://github.com/riza-io/riza-api-python/compare/v0.4.0...v0.5.0)

### Features

* **api:** api update ([#102](https://github.com/riza-io/riza-api-python/issues/102)) ([c8ea4ee](https://github.com/riza-io/riza-api-python/commit/c8ea4ee239378ce5b9da4d09632e92aa6888701b))
* **api:** api update ([#103](https://github.com/riza-io/riza-api-python/issues/103)) ([dd6e86b](https://github.com/riza-io/riza-api-python/commit/dd6e86b17f2be98752d94f957416ceec9869eaed))
* **api:** api update ([#98](https://github.com/riza-io/riza-api-python/issues/98)) ([f7f7d5f](https://github.com/riza-io/riza-api-python/commit/f7f7d5f97e98b6b6ab7c6f83322c76ba732a4ca7))


### Bug Fixes

* **client:** only call .close() when needed ([#99](https://github.com/riza-io/riza-api-python/issues/99)) ([2f1bc2d](https://github.com/riza-io/riza-api-python/commit/2f1bc2d99cc4abf2f1c5dcb37b8c560f466b0eae))
* correctly handle deserialising `cls` fields ([#104](https://github.com/riza-io/riza-api-python/issues/104)) ([3dcd14e](https://github.com/riza-io/riza-api-python/commit/3dcd14ed7378af31b405bdeb882460bbe838364c))


### Chores

* add missing isclass check ([#96](https://github.com/riza-io/riza-api-python/issues/96)) ([eb92ef8](https://github.com/riza-io/riza-api-python/commit/eb92ef8ac93da94d0dd5ce52b985f8732a5dc81f))
* **client:** simplify `Optional[object]` to just `object` ([#95](https://github.com/riza-io/riza-api-python/issues/95)) ([3f86041](https://github.com/riza-io/riza-api-python/commit/3f86041e44d871aeab2f6986d2f1702ddf0a9515))
* **internal:** bump httpx dependency ([#97](https://github.com/riza-io/riza-api-python/issues/97)) ([a68c310](https://github.com/riza-io/riza-api-python/commit/a68c310a4745d94238e5ef8af46fc2f2dbd3e5ab))
* **internal:** codegen related update ([#101](https://github.com/riza-io/riza-api-python/issues/101)) ([cc3e865](https://github.com/riza-io/riza-api-python/commit/cc3e8654246ab7afdd0f887f1de7b25c651e59bd))
* **internal:** codegen related update ([#93](https://github.com/riza-io/riza-api-python/issues/93)) ([f5ad741](https://github.com/riza-io/riza-api-python/commit/f5ad74129fdfc41d5355cba9e0c8f49912cdb0c4))


### Documentation

* fix typos ([#100](https://github.com/riza-io/riza-api-python/issues/100)) ([aa496ac](https://github.com/riza-io/riza-api-python/commit/aa496acaa98ecf9e04acf2e8a1b1160ac18d51bf))

## 0.4.0 (2024-12-18)

Full Changelog: [v0.3.0...v0.4.0](https://github.com/riza-io/riza-api-python/compare/v0.3.0...v0.4.0)

### Features

* **api:** api update ([#89](https://github.com/riza-io/riza-api-python/issues/89)) ([f1f8595](https://github.com/riza-io/riza-api-python/commit/f1f85956fa1cfc98b1e6086332fc95d256a7522a))
* **api:** api update ([#90](https://github.com/riza-io/riza-api-python/issues/90)) ([12c11ca](https://github.com/riza-io/riza-api-python/commit/12c11cad4477f0e887adda5335303b22da5838de))
* **api:** api update ([#91](https://github.com/riza-io/riza-api-python/issues/91)) ([d1474cb](https://github.com/riza-io/riza-api-python/commit/d1474cb5e34764f4de4355624f0dedf1d0682b9e))


### Chores

* **internal:** add support for TypeAliasType ([#81](https://github.com/riza-io/riza-api-python/issues/81)) ([0316272](https://github.com/riza-io/riza-api-python/commit/0316272914906914398463cd65121bf268187e33))
* **internal:** bump pydantic dependency ([#77](https://github.com/riza-io/riza-api-python/issues/77)) ([d92850c](https://github.com/riza-io/riza-api-python/commit/d92850cae7dc78d920b5964987aa59101123694f))
* **internal:** bump pyright ([#80](https://github.com/riza-io/riza-api-python/issues/80)) ([dc28972](https://github.com/riza-io/riza-api-python/commit/dc289729d0b73f6c5bd7b9486f2819fce8c025cb))
* **internal:** codegen related update ([#82](https://github.com/riza-io/riza-api-python/issues/82)) ([0f68452](https://github.com/riza-io/riza-api-python/commit/0f68452524594780e233204ace148c6f7695392b))
* **internal:** codegen related update ([#83](https://github.com/riza-io/riza-api-python/issues/83)) ([35024d0](https://github.com/riza-io/riza-api-python/commit/35024d0f2b31ff770555b545defa4a97f35c07aa))
* **internal:** codegen related update ([#84](https://github.com/riza-io/riza-api-python/issues/84)) ([56c8c66](https://github.com/riza-io/riza-api-python/commit/56c8c6632af5028f0f68fa5ffdfb3e010c56e950))
* **internal:** codegen related update ([#87](https://github.com/riza-io/riza-api-python/issues/87)) ([52e2d7c](https://github.com/riza-io/riza-api-python/commit/52e2d7cbf623e8fe04488a5869bbc9cefdafe730))
* **internal:** fix some typos ([#86](https://github.com/riza-io/riza-api-python/issues/86)) ([1e56043](https://github.com/riza-io/riza-api-python/commit/1e560433b42a231cdd18721fb3fb7dd0f21c601f))
* **internal:** fix some typos ([#88](https://github.com/riza-io/riza-api-python/issues/88)) ([75db94a](https://github.com/riza-io/riza-api-python/commit/75db94a3b5b7106e06bd2ecadb6ca6b657496b2c))


### Documentation

* **readme:** example snippet for client context manager ([#85](https://github.com/riza-io/riza-api-python/issues/85)) ([6154b28](https://github.com/riza-io/riza-api-python/commit/6154b2879402dfd19ff139bc99b77d486c8694dd))
* **readme:** fix http client proxies example ([#79](https://github.com/riza-io/riza-api-python/issues/79)) ([8f08d2b](https://github.com/riza-io/riza-api-python/commit/8f08d2bc7f92109d1445d159e1724198dc8b5770))

## 0.3.0 (2024-12-04)

Full Changelog: [v0.2.0...v0.3.0](https://github.com/riza-io/riza-api-python/compare/v0.2.0...v0.3.0)

### Features

* **api:** api update ([#65](https://github.com/riza-io/riza-api-python/issues/65)) ([eba3a1f](https://github.com/riza-io/riza-api-python/commit/eba3a1f7707ac227cb6aea17fa9a01eaf7a2ceb6))
* **api:** api update ([#73](https://github.com/riza-io/riza-api-python/issues/73)) ([ed2dce2](https://github.com/riza-io/riza-api-python/commit/ed2dce226c51ad686d5ac3f16eb415219f49e3d8))


### Bug Fixes

* **asyncify:** avoid hanging process under certain conditions ([#67](https://github.com/riza-io/riza-api-python/issues/67)) ([21f1add](https://github.com/riza-io/riza-api-python/commit/21f1add3810506b951b26234794e2e9861de746a))
* **client:** compat with new httpx 0.28.0 release ([#72](https://github.com/riza-io/riza-api-python/issues/72)) ([23c7fc1](https://github.com/riza-io/riza-api-python/commit/23c7fc19abd259d6079e21dc4bca7214e5b93eee))


### Chores

* **internal:** bump pyright ([#74](https://github.com/riza-io/riza-api-python/issues/74)) ([cf46ef4](https://github.com/riza-io/riza-api-python/commit/cf46ef43dbfef1afb9abd7187668b276b2b663f8))
* **internal:** exclude mypy from running on tests ([#71](https://github.com/riza-io/riza-api-python/issues/71)) ([eb486dd](https://github.com/riza-io/riza-api-python/commit/eb486dd086c91bf95ed2a6832eee87814520bddb))
* **internal:** fix compat model_dump method when warnings are passed ([#68](https://github.com/riza-io/riza-api-python/issues/68)) ([97dfabe](https://github.com/riza-io/riza-api-python/commit/97dfabe83694b0e25374bb4b092e3d4d9c8aa3d3))
* make the `Omit` type public ([#75](https://github.com/riza-io/riza-api-python/issues/75)) ([fb119ae](https://github.com/riza-io/riza-api-python/commit/fb119aee18caca678e0d9b9ef0cb9d87e825e04c))
* rebuild project due to codegen change ([#63](https://github.com/riza-io/riza-api-python/issues/63)) ([ddd46bc](https://github.com/riza-io/riza-api-python/commit/ddd46bc6dfb9e423aacc494b6a2a2205800d6ac5))
* rebuild project due to codegen change ([#66](https://github.com/riza-io/riza-api-python/issues/66)) ([d9dc13d](https://github.com/riza-io/riza-api-python/commit/d9dc13d8e1f112c70ece5466346d3e0dfabe6a75))
* remove now unused `cached-property` dep ([#70](https://github.com/riza-io/riza-api-python/issues/70)) ([767194b](https://github.com/riza-io/riza-api-python/commit/767194b1bf69905470c1d949118471f3fbca2934))


### Documentation

* add info log level to readme ([#69](https://github.com/riza-io/riza-api-python/issues/69)) ([0b9f395](https://github.com/riza-io/riza-api-python/commit/0b9f39590eb72bf13f56643f58a4b4059d2dbdd8))

## 0.2.0 (2024-11-07)

Full Changelog: [v0.1.1...v0.2.0](https://github.com/riza-io/riza-api-python/compare/v0.1.1...v0.2.0)

### Features

* **api:** api update ([#58](https://github.com/riza-io/riza-api-python/issues/58)) ([688cb10](https://github.com/riza-io/riza-api-python/commit/688cb109640323f2608fb996ff82129d334f225d))
* **api:** api update ([#61](https://github.com/riza-io/riza-api-python/issues/61)) ([7c8f2ee](https://github.com/riza-io/riza-api-python/commit/7c8f2ee4c54ebc950a559c76becc982519a03e53))
* **api:** manual updates ([#60](https://github.com/riza-io/riza-api-python/issues/60)) ([3b818f9](https://github.com/riza-io/riza-api-python/commit/3b818f95469ee73b5a80bda1cf127b71eecf90ce))

## 0.1.1 (2024-11-06)

Full Changelog: [v0.1.0-alpha.10...v0.1.1](https://github.com/riza-io/riza-api-python/compare/v0.1.0-alpha.10...v0.1.1)

### Features

* **api:** api update ([#48](https://github.com/riza-io/riza-api-python/issues/48)) ([1745365](https://github.com/riza-io/riza-api-python/commit/1745365fe3277da2bd55a46b5a5f1dd0d24f12e4))
* **api:** api update ([#50](https://github.com/riza-io/riza-api-python/issues/50)) ([8306dff](https://github.com/riza-io/riza-api-python/commit/8306dff6fc5dbcf7b1182d12789e2df7a03f87b9))
* **api:** api update ([#51](https://github.com/riza-io/riza-api-python/issues/51)) ([653755c](https://github.com/riza-io/riza-api-python/commit/653755cf38b346d996c526b28cb735a19e070a66))
* **api:** api update ([#53](https://github.com/riza-io/riza-api-python/issues/53)) ([314b137](https://github.com/riza-io/riza-api-python/commit/314b1375da1e8c34541d7ecbc6a3f119cb27636f))
* **api:** api update ([#54](https://github.com/riza-io/riza-api-python/issues/54)) ([feb4f33](https://github.com/riza-io/riza-api-python/commit/feb4f33a6ff1f192aae704531e06b180719b2006))
* **api:** api update ([#56](https://github.com/riza-io/riza-api-python/issues/56)) ([9285f7f](https://github.com/riza-io/riza-api-python/commit/9285f7f0ed4348d8445b75b7074cc4c87a906bac))
* **api:** manual updates ([#49](https://github.com/riza-io/riza-api-python/issues/49)) ([96c290a](https://github.com/riza-io/riza-api-python/commit/96c290ac6e12be6143ba9b795b98bf940f207f62))


### Bug Fixes

* **client:** avoid OverflowError with very large retry counts ([#46](https://github.com/riza-io/riza-api-python/issues/46)) ([4c7fd4f](https://github.com/riza-io/riza-api-python/commit/4c7fd4f2bcaf887fee0b364dca19ed7721781b61))


### Chores

* add repr to PageInfo class ([#47](https://github.com/riza-io/riza-api-python/issues/47)) ([67459c0](https://github.com/riza-io/riza-api-python/commit/67459c06bf0664e183acad544e9f8696acef6032))
* **internal:** add support for parsing bool response content ([#44](https://github.com/riza-io/riza-api-python/issues/44)) ([d908040](https://github.com/riza-io/riza-api-python/commit/d9080404367104b245c60255b7288e8941044850))
* **internal:** codegen related update ([#43](https://github.com/riza-io/riza-api-python/issues/43)) ([aa685cb](https://github.com/riza-io/riza-api-python/commit/aa685cb665ddebbfcfa97ce11124d29970571f29))
* rebuild project due to codegen change ([#52](https://github.com/riza-io/riza-api-python/issues/52)) ([c96d6bc](https://github.com/riza-io/riza-api-python/commit/c96d6bc5b781bc1a6ff18b1407247ddbfe89ffa9))
* rebuild project due to codegen change ([#55](https://github.com/riza-io/riza-api-python/issues/55)) ([6a4c4a5](https://github.com/riza-io/riza-api-python/commit/6a4c4a574d5b0b8360d612ccbade12b0346f777b))

## 0.1.0-alpha.10 (2024-09-18)

Full Changelog: [v0.1.0-alpha.9...v0.1.0-alpha.10](https://github.com/riza-io/riza-api-python/compare/v0.1.0-alpha.9...v0.1.0-alpha.10)

### Chores

* clean up dangling file ([fe7c4c9](https://github.com/riza-io/riza-api-python/commit/fe7c4c9c52e85961e0ccb20f3bc1655369997600))
* update SDK settings ([#41](https://github.com/riza-io/riza-api-python/issues/41)) ([9fdf24a](https://github.com/riza-io/riza-api-python/commit/9fdf24a229393691a08dd2c4ad2bbfdfbc98c13f))

## 0.1.0-alpha.9 (2024-09-13)

Full Changelog: [v0.1.0-alpha.8...v0.1.0-alpha.9](https://github.com/riza-io/riza-api-python/compare/v0.1.0-alpha.8...v0.1.0-alpha.9)

### Features

* **api:** OpenAPI spec update via Stainless API ([#33](https://github.com/riza-io/riza-api-python/issues/33)) ([da968f6](https://github.com/riza-io/riza-api-python/commit/da968f6116ea69d3f18779b86ae7e5a46408497d))


### Chores

* add docstrings to raw response properties ([#35](https://github.com/riza-io/riza-api-python/issues/35)) ([3296fbc](https://github.com/riza-io/riza-api-python/commit/3296fbcd7a63f514ac06a6c5f050da6ccc27b1bf))
* **ci:** limit release doctor target branches ([#29](https://github.com/riza-io/riza-api-python/issues/29)) ([4c0b46c](https://github.com/riza-io/riza-api-python/commit/4c0b46c06ba58f0d9b1c84bf338cb13b173c7b12))
* **docs:** document how to do per-request http client customization ([#28](https://github.com/riza-io/riza-api-python/issues/28)) ([15f7718](https://github.com/riza-io/riza-api-python/commit/15f77183f7f8069f65f69f9bdbe87c6fdb501676))
* **internal:** codegen related update ([#34](https://github.com/riza-io/riza-api-python/issues/34)) ([213c89e](https://github.com/riza-io/riza-api-python/commit/213c89e14a3dc14d8d14a7afeafa27c25f9e9ed6))
* **internal:** codegen related update ([#37](https://github.com/riza-io/riza-api-python/issues/37)) ([31ce301](https://github.com/riza-io/riza-api-python/commit/31ce301dea3fb6451f8d6684d0340dca9734ff38))
* **internal:** refactor release doctor script ([#31](https://github.com/riza-io/riza-api-python/issues/31)) ([afaf9cf](https://github.com/riza-io/riza-api-python/commit/afaf9cff9d0040728ec6ffc5b292bd0cdc53d439))
* remove custom code ([1086ca7](https://github.com/riza-io/riza-api-python/commit/1086ca7698b20f8bede98a41725b91a0eeb3dcbf))
* **tests:** update prism version ([#32](https://github.com/riza-io/riza-api-python/issues/32)) ([82c2c7d](https://github.com/riza-io/riza-api-python/commit/82c2c7daf2271cd2898346af14bd4988635b3de0))


### Documentation

* **readme:** add section on determining installed version ([#36](https://github.com/riza-io/riza-api-python/issues/36)) ([81fec16](https://github.com/riza-io/riza-api-python/commit/81fec16ebcd3fb6d26d3bab2dea3c1ed18134683))
* update CONTRIBUTING.md ([#38](https://github.com/riza-io/riza-api-python/issues/38)) ([5f9e19c](https://github.com/riza-io/riza-api-python/commit/5f9e19c50a08758c1025a7ae30020803c6704eab))

## 0.1.0-alpha.8 (2024-07-23)

Full Changelog: [v0.1.0-alpha.7...v0.1.0-alpha.8](https://github.com/riza-io/riza-api-python/compare/v0.1.0-alpha.7...v0.1.0-alpha.8)

### Features

* **api:** OpenAPI spec update via Stainless API ([#23](https://github.com/riza-io/riza-api-python/issues/23)) ([2004d59](https://github.com/riza-io/riza-api-python/commit/2004d599a7d953a0525d9e178f64a90f5f818d64))


### Chores

* **docs:** minor update to formatting of API link in README ([#27](https://github.com/riza-io/riza-api-python/issues/27)) ([6d48304](https://github.com/riza-io/riza-api-python/commit/6d4830432b9ec27c7160a7a563317cc74eddcf18))
* **internal:** codegen related update ([#24](https://github.com/riza-io/riza-api-python/issues/24)) ([216fe46](https://github.com/riza-io/riza-api-python/commit/216fe463845c8478895564cc052ae67c615e3c8f))
* **internal:** minor options / compat functions updates ([#26](https://github.com/riza-io/riza-api-python/issues/26)) ([6daa3f5](https://github.com/riza-io/riza-api-python/commit/6daa3f5dec20cce35c769c830205100fe8296a90))

## 0.1.0-alpha.7 (2024-05-22)

Full Changelog: [v0.1.0-alpha.6...v0.1.0-alpha.7](https://github.com/riza-io/riza-api-python/compare/v0.1.0-alpha.6...v0.1.0-alpha.7)

### Features

* **api:** OpenAPI spec update via Stainless API ([#19](https://github.com/riza-io/riza-api-python/issues/19)) ([0264f17](https://github.com/riza-io/riza-api-python/commit/0264f1720a39108489060c2621c5d0f1eead298f))
* **api:** OpenAPI spec update via Stainless API ([#21](https://github.com/riza-io/riza-api-python/issues/21)) ([307af07](https://github.com/riza-io/riza-api-python/commit/307af072f1c6babe273f106e77487ab4be84f01d))

## 0.1.0-alpha.6 (2024-04-23)

Full Changelog: [v0.1.0-alpha.5...v0.1.0-alpha.6](https://github.com/riza-io/riza-api-python/compare/v0.1.0-alpha.5...v0.1.0-alpha.6)

### Features

* **api:** update via SDK Studio ([#17](https://github.com/riza-io/riza-api-python/issues/17)) ([cf7aa3b](https://github.com/riza-io/riza-api-python/commit/cf7aa3bc0732faed46e89f6606e968c4f3f01f87))

## 0.1.0-alpha.5 (2024-04-19)

Full Changelog: [v0.1.0-alpha.4...v0.1.0-alpha.5](https://github.com/riza-io/riza-api-python/compare/v0.1.0-alpha.4...v0.1.0-alpha.5)

### Features

* **api:** OpenAPI spec update via Stainless API ([#15](https://github.com/riza-io/riza-api-python/issues/15)) ([cce36c0](https://github.com/riza-io/riza-api-python/commit/cce36c0b4cb84cf1ba6fe91c77df4117833dcea3))

## 0.1.0-alpha.4 (2024-04-18)

Full Changelog: [v0.1.0-alpha.3...v0.1.0-alpha.4](https://github.com/riza-io/riza-api-python/compare/v0.1.0-alpha.3...v0.1.0-alpha.4)

### Features

* **api:** update via SDK Studio ([#13](https://github.com/riza-io/riza-api-python/issues/13)) ([b8df108](https://github.com/riza-io/riza-api-python/commit/b8df10863e947363a911582eeee371f67db20ca0))

## 0.1.0-alpha.3 (2024-04-18)

Full Changelog: [v0.1.0-alpha.2...v0.1.0-alpha.3](https://github.com/riza-io/riza-api-python/compare/v0.1.0-alpha.2...v0.1.0-alpha.3)

### Features

* **api:** update via SDK Studio ([#11](https://github.com/riza-io/riza-api-python/issues/11)) ([b1a00ad](https://github.com/riza-io/riza-api-python/commit/b1a00adc91789b33848b241db2df14fa10e21cdc))
* **api:** update via SDK Studio ([#12](https://github.com/riza-io/riza-api-python/issues/12)) ([7abe327](https://github.com/riza-io/riza-api-python/commit/7abe3271497b4b25ebae4968f9e5983d23cd5509))
* **api:** update via SDK Studio ([#7](https://github.com/riza-io/riza-api-python/issues/7)) ([2f007bc](https://github.com/riza-io/riza-api-python/commit/2f007bc3355bfa36e7e056fd890635f4549e8d7c))
* **api:** update via SDK Studio ([#9](https://github.com/riza-io/riza-api-python/issues/9)) ([9608f97](https://github.com/riza-io/riza-api-python/commit/9608f9709fe4df610841daae63170dd47740b8b5))

## 0.1.0-alpha.2 (2024-04-18)

Full Changelog: [v0.1.0-alpha.1...v0.1.0-alpha.2](https://github.com/riza-io/riza-api-python/compare/v0.1.0-alpha.1...v0.1.0-alpha.2)

### Features

* **api:** update via SDK Studio ([#4](https://github.com/riza-io/riza-api-python/issues/4)) ([c935203](https://github.com/riza-io/riza-api-python/commit/c9352037d128ddf9a11ffd70b69143d1f1bbb74b))

## 0.1.0-alpha.1 (2024-04-17)

Full Changelog: [v0.0.1-alpha.0...v0.1.0-alpha.1](https://github.com/riza-io/riza-api-python/compare/v0.0.1-alpha.0...v0.1.0-alpha.1)

### Features

* **api:** update via SDK Studio ([2cb36e7](https://github.com/riza-io/riza-api-python/commit/2cb36e72a9fce9afc70ddc77cc45407dfdf0f862))
* **api:** update via SDK Studio ([43548b9](https://github.com/riza-io/riza-api-python/commit/43548b96188d5222bbe0a24c5bc1a289af61f3ef))


### Chores

* configure new SDK language ([e3b9655](https://github.com/riza-io/riza-api-python/commit/e3b9655672239194b90a9ed5fe585a46333ed13a))
* go live ([#1](https://github.com/riza-io/riza-api-python/issues/1)) ([392c011](https://github.com/riza-io/riza-api-python/commit/392c011821527c8f10a4f4618a2059aa3d8acc92))
* update SDK settings ([#3](https://github.com/riza-io/riza-api-python/issues/3)) ([efe8506](https://github.com/riza-io/riza-api-python/commit/efe85061f7268254a34659958a511b9d85d1454a))
