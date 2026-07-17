---
title: "Local Delegated Agent Identity Architecture"
abbrev: "Local Delegated Agent Identity"
docname: draft-1password-agent-identity-local-delegated-00
category: info
submissiontype: independent
ipr: trust200902
date: 2026-04
v: 3
area: SEC
keyword:
 - AI agents
 - delegation
 - OAuth
 - WIMSE
 - DPoP
 - transaction tokens

author:
 -
    fullname: J. Malnick
    organization: 1Password
 -
    fullname: J. Meller
    organization: 1Password
 -
    fullname: R. Menke
    organization: 1Password

normative:
  RFC2119:
  RFC8174:
  RFC6749:
  RFC7519:
  RFC7591:
  RFC7636:
  RFC8693:
  RFC9068:
  RFC9421:
  RFC9449:
  RFC9700:
  OIDC-Core:
    title: "OpenID Connect Core 1.0 incorporating errata set 2"
    target: https://openid.net/specs/openid-connect-core-1_0.html
    author:
      - fullname: N. Sakimura
      - fullname: J. Bradley
      - fullname: M. Jones
      - fullname: B. de Medeiros
      - fullname: C. Mortimore
    date: 2014-11
  NIST-63-4:
    title: "NIST SP 800-63-4 Digital Identity Guidelines"
    target: https://pages.nist.gov/800-63-4/
    author:
      - organization: NIST
    date: 2025-07
  NIST-207:
    title: "NIST SP 800-207 Zero Trust Architecture"
    target: https://csrc.nist.gov/publications/detail/sp/800-207/final
    author:
      - organization: NIST
    date: 2020-08

informative:
  RATS-ARCH:
    title: "Remote Attestation Procedures (RATS) Architecture"
    target: https://www.rfc-editor.org/info/rfc9334
    seriesinfo:
      RFC: "9334"
    author:
      - fullname: H. Birkholz
    date: 2023-01
  RFC8252:
  OAUTH-v2.1:
    title: "The OAuth 2.1 Authorization Framework"
    target: https://datatracker.ietf.org/doc/draft-ietf-oauth-v2-1/
    seriesinfo:
      Internet-Draft: draft-ietf-oauth-v2-1-15
    author:
      - fullname: D. Hardt
      - fullname: A. Parecki
      - fullname: T. Lodderstedt
    date: 2026-03
  OAUTH-TXN-TOKENS:
    title: "Transaction Tokens"
    target: https://datatracker.ietf.org/doc/draft-ietf-oauth-transaction-tokens/
    seriesinfo:
      Internet-Draft: draft-ietf-oauth-transaction-tokens-08
    author:
      - fullname: A. Tulshibagwale
      - fullname: G. Fletcher
      - fullname: P. Kasselman
    date: 2026-03
  OAUTH-TXN-AGENTS:
    title: "Transaction Tokens For Agents"
    target: https://datatracker.ietf.org/doc/draft-oauth-transaction-tokens-for-agents/
    seriesinfo:
      Internet-Draft: draft-oauth-transaction-tokens-for-agents-00
    author:
      - organization: RAUT
    date: 2025-11
  TXN-AGENTS-GATEWAY:
    title: "Transaction Tokens For Agents (Gateway Profile)"
    target: https://datatracker.ietf.org/doc/draft-araut-oauth-transaction-tokens-for-agents/
    author:
      - fullname: A. Araut
    seriesinfo:
      Internet-Draft: draft-araut-oauth-transaction-tokens-for-agents
  OAUTH-CHAIN:
    title: "OAuth Identity and Authorization Chaining Across Domains"
    target: https://datatracker.ietf.org/doc/draft-ietf-oauth-identity-chaining/
    seriesinfo:
      Internet-Draft: draft-ietf-oauth-identity-chaining-08
    author:
      - fullname: A. Schwenkschuster
    date: 2026-02
  OAUTH-ID-JAG:
    title: "Identity Assertion JWT Authorization Grant"
    target: https://datatracker.ietf.org/doc/draft-ietf-oauth-identity-assertion-authz-grant/
    seriesinfo:
      Internet-Draft: draft-ietf-oauth-identity-assertion-authz-grant-02
    author:
      - fullname: A. Parecki
    date: 2026-03
  OAUTH-ATTEST:
    title: "OAuth 2.0 Attestation-Based Client Authentication"
    target: https://datatracker.ietf.org/doc/draft-ietf-oauth-attestation-based-client-auth/
    seriesinfo:
      Internet-Draft: draft-ietf-oauth-attestation-based-client-auth
    author:
      - fullname: T. Looker
    date: 2026
  AI-AUTH:
    title: "AI Agent Authentication and Authorization"
    target: https://datatracker.ietf.org/doc/draft-klrc-aiagent-auth/
    seriesinfo:
      Internet-Draft: draft-klrc-aiagent-auth-01
    author:
      - fullname: P. Kasselman
      - fullname: J.-F. Lombardo
      - fullname: Y. Rosomakho
      - fullname: B. Campbell
      - fullname: N. Steele
    date: 2026-03
  WIMSE-ARCH:
    title: "Workload Identity in a Multi System Environment (WIMSE) Architecture"
    target: https://datatracker.ietf.org/doc/draft-ietf-wimse-arch/
    seriesinfo:
      Internet-Draft: draft-ietf-wimse-arch-07
    author:
      - fullname: J. Salowey
    date: 2026-03
  WIMSE-IDENTIFIER:
    title: "Workload Identifier"
    target: https://datatracker.ietf.org/doc/draft-ietf-wimse-identifier/
    seriesinfo:
      Internet-Draft: draft-ietf-wimse-identifier-01
    author:
      - fullname: Y. Rosomakho
      - fullname: J. Salowey
    date: 2025-12
  WIMSE-CREDS:
    title: "WIMSE Workload Credentials"
    target: https://datatracker.ietf.org/doc/draft-ietf-wimse-workload-creds/
    seriesinfo:
      Internet-Draft: draft-ietf-wimse-workload-creds-00
    author:
      - fullname: B. Campbell
    date: 2025-11
  WIMSE-S2S:
    title: "WIMSE Workload-to-Workload Authentication"
    target: https://datatracker.ietf.org/doc/draft-ietf-wimse-s2s-protocol/
    seriesinfo:
      Internet-Draft: draft-ietf-wimse-s2s-protocol-07
    author:
      - fullname: B. Campbell
    date: 2025-10
  WIMSE-HTTP-SIG:
    title: "WIMSE Workload-to-Workload Authentication with HTTP Signatures"
    target: https://datatracker.ietf.org/doc/draft-ietf-wimse-http-signature/
    seriesinfo:
      Internet-Draft: draft-ietf-wimse-http-signature-03
    author:
      - fullname: J. Salowey
      - fullname: Y. Sheffer
    date: 2026-04
  SPIFFE:
    title: "Secure Production Identity Framework for Everyone (SPIFFE)"
    target: https://spiffe.io/docs/latest/spiffe-about/spiffe-concepts/
    author:
      - organization: CNCF
    date: 2023
  WebAuthn-L3:
    title: "Web Authentication: An API for accessing Public Key Credentials - Level 3"
    target: https://www.w3.org/TR/webauthn-3/
    author:
      - organization: W3C
    date: 2025
  FIDO2-CTAP:
    title: "Client to Authenticator Protocol (CTAP) 2.1 Proposed Standard"
    target: https://fidoalliance.org/specs/fido-v2.1-ps-20210615/fido-client-to-authenticator-protocol-v2.1-ps-20210615.html
    author:
      - organization: FIDO Alliance
    date: 2021-06
  CAEP:
    title: "OpenID Continuous Access Evaluation Profile 1.0 - Final"
    target: https://openid.net/specs/openid-caep-1_0.html
    author:
      - organization: OpenID Foundation
    date: 2023
  NIST-AIMS:
    title: "Accelerating the Adoption of Software and AI Agent Identity and Authorization - Concept Paper"
    target: https://www.nccoe.nist.gov/
    author:
      - organization: NIST NCCoE
    date: 2026-02
  MCP:
    title: "Model Context Protocol Specification"
    target: https://modelcontextprotocol.io/specification
    author:
      - organization: Anthropic
    date: 2024
  OS-Workload-Attestation:
    title: "OS-Level Workload Attestation"
    target: https://datatracker.ietf.org/doc/draft-1password-os-level-workload-attestation/
    seriesinfo:
      Internet-Draft: draft-1password-os-level-workload-attestation-00
    author:
      - fullname: J. Meller
      - fullname: J. Malnick
    date: 2026-04

--- abstract

This document specifies a reference architecture for the Agent
Identity Management System (AIMS) conceptual model, as introduced in
the NIST concept paper {{NIST-AIMS}} and elaborated in {{AI-AUTH}},
applied to the local delegated agent profile. It defines the identity
architecture for delegated AI agents that execute on end-user devices
(laptops, desktops) or in browser-based sandboxes, acting on behalf of
a technical user. The architecture composes existing and emerging
IETF, W3C, FIDO Alliance, and OpenID specifications, supplemented by
the OS-level peer-process verification protocol of the companion
document {{OS-Workload-Attestation}}, to realize each of the seven
AIMS functions: Identifier, Credentials, Attestation, Provisioning,
Authentication, Authorization, and Monitoring. Section 4.4 maps each
AIMS function to the section of this document that realizes it.

This document is a reference architecture, not a protocol
specification. It does not define new wire protocols; it defines how
to compose existing ones for this profile. Vendor-specific extensions
encountered during reference-implementation work, most notably a
custom delegation-relationship identifier and proof-of-possession
mechanisms for the delegated access token, have been deliberately
excluded from this revision and deferred to separate work, so that the
architecture is grounded only in capabilities that exist in shipping
or actively-drafted specifications today.

Security gaps inherent to the local trust boundary are enumerated
alongside candidate mitigations.

This document is the first in a six-part series specifying a reference
architecture for AI agent identity across three authority models, each
with a local and a remote variant. The three authority models are:
human-delegated agents, which act on behalf of a present human Subject
under that Subject's explicit consent; machine- or application-bounded
agents, which act under the authority of a system or workflow rather
than a specific human and are constrained to a pre-declared scope; and
fully autonomous agents, which pursue a goal over time with minimal
direct human oversight. Each model has a local variant (executing on
an end-user device or in a browser sandbox) and a remote variant
(executing in managed cloud compute), yielding the six combinations
covered by the series. This document covers the local human-delegated
profile.

Companion documents, most notably {{OS-Workload-Attestation}} for
OS-level peer verification and the Remote Delegated companion for the
cloud-managed compute profile, share the AIMS framing and refer to
this document for the local-delegated-specific composition.

--- middle

# Introduction and Scope {#introduction-and-scope}

## Profile and Audience {#profile-and-audience}

AI agents operating in the delegated authority model
act on behalf of a human Subject, inheriting that Subject’s permissions
and executing tasks within the scope of an explicit delegation. This
document addresses the specific variant in which such an agent runs
locally: either as a native process on a user’s machine (laptop,
desktop, or technical workstation) or within a browser-origin sandbox
(web application, browser extension, or WebAssembly module).

These environments share a defining characteristic: the
agent executable and any keys it manages reside in a space controlled by
the end user, not by a managed infrastructure provider. This creates a
fundamentally different threat model compared to a remote agent running
inside a cloud-controlled compute environment:

- The execution environment is not hardware-attested by
  default. No trusted execution environment (TEE) or TPM binding to a
  managed compute node is available.
- The user is physically present and typically
  initiates the agent interactively, which enables human-in-the-loop
  consent flows unavailable in headless cloud deployments.
- Secret material (tokens, keys) is at elevated risk
  from local credential theft, process injection, and memory scraping by
  other processes running under the same OS user account.
- Browser-based agents additionally face origin-bound
  credential scoping, malicious extensions, cross-origin leakage, and
  prompt injection via DOM manipulation.

Despite these constraints, the local delegated agent is
among the most prevalent agent patterns today: AI coding agents (e.g.,
terminal-based agentic tools that query upstream APIs and execute
commands on behalf of a user), local LLM orchestrators, and
IDE-integrated assistants all fit this profile.

<aside markdown="1">
**Scope Note**

This document covers: (a) native local process
agents, and (b) browser-sandbox agents. It does not cover mobile apps
(addressed in a future appendix), server-side agents operating inside
managed cloud environments (see Remote Delegated, doc 2 of 6), or
sub-agents spawned by another agent (see Bounded/Autonomous, docs 3 to
6).
</aside>

## Relationship to AIMS {#relationship-to-aims}

The Agent Identity Management System (AIMS) conceptual
model originates in the NIST concept paper {{NIST-AIMS}} and is
elaborated as a normative seven-function framework in {{AI-AUTH}}. AIMS
describes the set of functions required to establish, maintain, and
evaluate the identity and permissions of an agent workload: Identifier,
Credentials, Attestation, Provisioning, Authentication, Authorization,
and Monitoring. AIMS itself is a model, not a wire protocol; it does not
prescribe the specific transports, token formats, or platform primitives
used to realize each function.

This document is a reference architecture for AIMS in
the local-delegated profile. Each AIMS function is bound to a concrete
specification or specification cluster: SPIFFE workload identifiers
{{SPIFFE}}, JWT-SVID credentials {{WIMSE-CREDS}}, OS-mediated peer
attestation per {{OS-Workload-Attestation}}, JIT credential provisioning
via the Workload API of {{OS-Workload-Attestation}} Section 3, OAuth
Token Exchange {{RFC8693}} for authentication, scope-attenuated
delegated access tokens with per-call `Txn-Token` {{OAUTH-TXN-TOKENS}}
propagation for authorization, and the audit and revocation surface of
Section 8 for monitoring. Where two or more profiles in the 1Password
agent identity series share an AIMS function realization, the
realization is specified once in the appropriate companion document and
referenced from each profile that uses it; where a function differs by
profile, this document specifies the local-delegated composition
explicitly.

Section 4.4 provides the AIMS function-to-section
mapping. Sections 5 through 8 correspond, in order, to the AIMS
functional groups of identity establishment, authentication,
authorization, and monitoring. Section 12 enumerates work deliberately
deferred from this revision.

## Conformance {#conformance}

An implementation conforms to this reference
architecture if it realizes each AIMS function as specified in the
corresponding section, satisfies the normative requirements of the
{{OS-Workload-Attestation}} companion (which this document references as
the realization of the Attestation and Provisioning functions), and does
not relax the security properties enumerated in Section 10. An
implementation that omits a function, for example by omitting Monitoring
or relaxing the per-issuance peer verification of
{{OS-Workload-Attestation}} Section 4, does not conform to this profile.
Implementations MAY add capabilities beyond those specified here (for
example, the deferred work enumerated in Section 12), provided the
additions do not weaken the security properties of any AIMS function
realized in this document.

# Conventions and Terminology {#conventions-and-terminology}

The key words MUST, MUST NOT, REQUIRED, SHOULD, SHOULD
NOT, RECOMMENDED, and MAY in this document are to be interpreted as
described in BCP 14 {{RFC2119}} {{RFC8174}}.

Agent: A workload capable of
LLM-guided reasoning and tool execution.

AIMS: Agent Identity
Management System. The conceptual seven-function model originating in
{{NIST-AIMS}} and elaborated in {{AI-AUTH}}. Functions: Identifier,
Credentials, Attestation, Provisioning, Authentication, Authorization,
Monitoring.

Subject: The technical user on
whose behalf the agent acts.

Delegation: The explicit,
scoped transfer of authority from Subject to Agent.

Local Agent: An agent process
running on the Subject’s device or in a browser origin controlled by the
Subject’s session.

Browser-Sandbox Agent: An
agent executing within a browser’s JavaScript / WASM origin. Treated as
equivalent to local agent for purposes of this document.

IdP: Identity Provider. Issues
identity tokens (ID tokens) about the Subject.

AS: Authorization Server.
Issues access tokens and manages authorization grants.

WIB: Workload Identity Broker.
The architectural component that brokers verifiable workload identity
for local agents. Specified in {{OS-Workload-Attestation}} and applied
in Section 5.2 of this document.

TTS: Transaction Token Service
{{OAUTH-TXN-TOKENS}}. Issues `Txn-Token`s scoped to a single transaction
call-chain.

`Txn-Token`: A short-lived,
signed JWT that propagates immutable identity and intent context through
a call chain.

WIMSE ID: A URI-format
workload identifier as defined in {{WIMSE-IDENTIFIER}}.

SPIFFE ID: The SPIFFE
realization of a workload identifier per {{SPIFFE}}. In this document,
the workload identifier scheme used to realize the AIMS Identifier
function.

JWT-SVID: A SPIFFE Verifiable
Identity Document encoded as a signed JSON Web Token. The credential
format used to realize the AIMS Credentials function.

PDP: Policy Decision Point.
Evaluates authorization policy against runtime signals.

PEP: Policy Enforcement Point.
Enforces decisions from the PDP.

PKCE: Proof Key for Code
Exchange {{RFC7636}}. Prevents authorization code interception attacks
in public clients.

act claim: JWT ‘actor’ claim
carrying the agent’s identifier, distinguishing it from the delegating
Subject.

Intent Binding: The
cryptographic association of a `Txn-Token` with the specific user-declared
goal that initiated the agent task.

Prompt Injection: An attack in
which adversarial content in agent tool outputs manipulates the LLM’s
subsequent actions beyond the user’s intended delegation scope.

# Protocol Reference Stack {#protocol-reference-stack}

The following table lists all normative and informative specifications referenced in this document. Status reflects standing as of April 2026. The AIMS source documents {{NIST-AIMS}} and {{AI-AUTH}} are listed first as the conceptual model this document realizes; the remaining entries are organized by AIMS function area where applicable.

| Tag | Title | Status | AIMS Function |
|---|---|---|---|
| {{NIST-AIMS}} | NIST AIMS Concept Paper | NIST Concept Paper | Model (all) |
| {{AI-AUTH}} | AI Agent Authentication and Authorization | I-D (Emerging) | Model (all) |
| {{OS-Workload-Attestation}} | OS-Level Workload Attestation | Companion (this series) | Attestation, Provisioning |
| {{SPIFFE}} | SPIFFE: Secure Production Identity Framework for Everyone | Standard (Informative) | Identifier, Credentials |
| {{WIMSE-IDENTIFIER}} | WIMSE Workload Identifier | I-D (Emerging) | Identifier |
| {{WIMSE-CREDS}} | WIMSE Workload Credentials | I-D (Emerging) | Credentials |
| {{WIMSE-ARCH}} | WIMSE Architecture | I-D (Emerging) | Identifier, Credentials |
| {{WIMSE-S2S}} | WIMSE Workload-to-Workload Authentication | I-D (Emerging) | Authentication |
| {{WIMSE-HTTP-SIG}} | WIMSE Workload-to-Workload Auth with HTTP Signatures | I-D (Emerging) | Authentication |
| {{RFC6749}} | OAuth 2.0 Authorization Framework | RFC (Normative) | Authentication, Authorization |
| {{RFC7636}} | PKCE for OAuth Public Clients | RFC (Normative) | Authentication |
| {{RFC8693}} | OAuth 2.0 Token Exchange | RFC (Normative) | Authentication |
| {{RFC9700}} | OAuth 2.0 Security BCP | RFC/BCP (Normative) | Authentication |
| {{RFC9068}} | JWT Profile for OAuth 2.0 Access Tokens | RFC (Normative) | Credentials |
| {{RFC7519}} | JSON Web Token (JWT) | RFC (Normative) | Credentials |
| {{RFC7591}} | OAuth 2.0 Dynamic Client Registration | RFC (Normative) | Provisioning |
| {{RFC9421}} | HTTP Message Signatures | RFC (Normative) | Authentication |
| {{OAUTH-v2.1}} | The OAuth 2.1 Authorization Framework | I-D (Informative) | Authentication |
| {{OAUTH-TXN-TOKENS}} | Transaction Tokens (`Txn-Token`s) | I-D (Emerging) | Authorization |
| {{OAUTH-TXN-AGENTS}} | Transaction Tokens For Agents | I-D (Emerging) | Authorization |
| {{OAUTH-CHAIN}} | OAuth Identity and Authorization Chaining Across Domains | I-D (Emerging) | Authorization |
| {{OAUTH-ID-JAG}} | Identity Assertion JWT Authorization Grant | I-D (Emerging) | Authentication |
| {{OAUTH-ATTEST}} | OAuth 2.0 Attestation-Based Client Authentication | I-D (Emerging) | Attestation |
| {{OIDC-Core}} | OpenID Connect Core 1.0 (errata 2) | Final (Normative) | Authentication |
| {{WebAuthn-L3}} | Web Authentication Level 3 | W3C Working Draft | Authentication |
| {{FIDO2-CTAP}} | FIDO2 Client-to-Authenticator Protocol (CTAP2) | FIDO Proposed Standard | Authentication |
| {{CAEP}} | OpenID Continuous Access Evaluation Profile 1.0 | OpenID Final | Monitoring, Authorization |
| {{NIST-63-4}} | NIST SP 800-63-4 Digital Identity Guidelines | NIST Final (July 2025) | Authentication |
| {{NIST-207}} | NIST SP 800-207 Zero Trust Architecture | NIST Final | Model (all) |
| {{RATS-ARCH}} | Remote Attestation Procedures (RATS) Architecture | RFC 9334 | Attestation |
| {{MCP}} | Model Context Protocol Specification | Informational | (reference) |

# Architecture Overview {#architecture-overview}

The local delegated agent architecture consists of the
following components operating within or adjacent to the local trust
boundary. Each component participates in one or more AIMS functions;
Section 4.4 enumerates the function-to-section mapping for the AIMS
reader.

## Component Inventory {#component-inventory}

- Human Subject : The
  technical user who initiates the agent task, provides consent, and
  retains ultimate authority over the agent’s delegated scope. Source of
  the AIMS Authentication input at consent time and of the user-presence
  assertions consumed by the Authorization function.
- Local Agent Process / Browser-Sandbox Agent
  : The local agent workload. Runs as a native
  OS process (e.g., a CLI tool, a desktop application, an Electron app)
  or as JavaScript / WASM inside a browser origin. Holds ephemeral
  credentials scoped to the delegated resource and a WIMSE-compatible
  identifier. The bearer of the AIMS Identifier and the consumer of AIMS
  Credentials issuance.
- Identity Provider (IdP) :
  Authenticates the human Subject and issues ID tokens (OIDC). Acts as
  the root of trust for the delegation chain. Realizes the human-side
  AIMS Authentication function. Typically a remote OIDC-compliant
  enterprise IdP accessed over TLS.
- Authorization Server (AS) :
  Issues access tokens scoped to specific resources and delegations.
  Operates as a federated relying party to the IdP for human
  authentication, and as the OAuth Authorization Server for downstream
  Resource Servers. Processes the Token Exchange (Section 7.1) that
  elevates the Subject’s federated access token into an agent-scoped
  delegated access token carrying the act claim. Validates WIB-issued
  JWT-SVIDs (Section 5.2) presented as actor\_token against its
  enrolled-WIB trust bundle. Realizes the agent-side AIMS Authentication
  and Authorization functions. The AS’s endpoint surface is detailed in
  Section 4.3.
- Workload Identity Broker (WIB)
  : A code-signed local daemon that mediates
  identity issuance to agent workloads on the Subject’s device. Holds a
  device-bound key pair enrolled with the AS (Section 5.2.2), exposes a
  SPIFFE-style Workload API to local agents per
  {{OS-Workload-Attestation}} Section 3, and issues short-lived
  JWT-SVIDs after performing OS-level peer-process verification per
  {{OS-Workload-Attestation}} Section 4. The WIB is the architectural
  component that realizes the AIMS Attestation function on unattested
  local hardware and the AIMS Provisioning function (JIT issuance per
  task). Specified in detail in Section 5.2.
- Transaction Token Service (TTS)
  : Issues short-lived `Txn-Token`s per
  {{OAUTH-TXN-TOKENS}} and {{OAUTH-TXN-AGENTS}}. Binds the transaction’s
  immutable context (subject identity, agent identity, user intent).
  Logically distinct from the AS, but typically realized as an
  additional endpoint on the AS within the same trust authority (Section
  4.3.4). Realizes the per-call leg of the AIMS Authorization function.
  The endpoint name and grant\_type semantics defined in
  {{OAUTH-TXN-TOKENS}} are an emerging Internet-Draft and SHOULD be
  expected to change. Each logical trust domain MUST have exactly one
  TTS.
- Policy Decision Point (PDP)
  : An architectural role per {{NIST-207}} and
  {{AI-AUTH}} Section 4. In this architecture, the PDP role is realized
  as policy evaluation embedded within the AS’s `/token` and `/txn-token`
  endpoints. Section 4.5 specifies the PDP’s position, inputs, and
  decision surfaces in detail.
- Policy Enforcement Point (PEP)
  : An architectural role per {{NIST-207}}.
  Realized by each Resource Server’s request-validation layer, which
  validates the access token’s signature and audience, the `Txn-Token`’s
  identity context and intent hash, and the requested action against the
  granted scope. Realizes the enforcement leg of the AIMS Authorization
  function and the per-call audit emission consumed by AIMS Monitoring
  (Section 8). The PEP is not a separately-deployed service in this
  architecture.
- Resource Server(s) : The
  upstream services the agent interacts with (APIs, databases, SaaS
  apps, MCP servers). Validate access tokens and / or `Txn-Token`s, and
  enforce resource-level access policy.
- Credential Store : A secure
  local secret store backed by the platform OS (macOS Keychain with
  Secure Enclave, Windows DPAPI / CNG with TPM, Linux Secret Service /
  TPM where available, or in-browser Web Crypto non-extractable keys).
  Used by the WIB to hold its enrolled device-bound key. The agent
  process itself does not hold long-lived asymmetric key material in
  this profile (the agent’s identity is established by presenting the
  WIB-issued SVID rather than by holding its own key); the Credential
  Store’s role here is to protect the WIB’s device key and any
  short-lived material the agent obtains from the AS. The substrate that
  protects AIMS Credentials at rest in the local trust domain.

## Trust Domains {#trust-domains}

This architecture spans two trust domains:

- Local Trust Domain : The
  agent process, the credential store, the WIB, and any locally-bound
  tool processes. Bounded by the OS user account / browser origin.
  Inherently lower assurance than a managed server environment.
- Remote Trust Domain : The
  IdP, AS, TTS, PDP, and Resource Servers. Operates in managed
  infrastructure. Connected to the Local Trust Domain over mutually
  authenticated TLS channels.

Tokens MUST NOT flow between trust domains without
validation at the boundary. The agent’s access token, minted by the
remote AS with the Subject’s delegation, crosses from Remote to Local
when delivered to the agent. The `Txn-Token`, once minted for a call
chain, crosses from Local to Remote with each API call.

<aside markdown="1">
**Architectural Constraint**

Because local agents cannot provide hardware-backed
TEE attestation, the remote AS and TTS MUST treat the local trust domain
as a lower-assurance environment. This is the AIMS Attestation function
operating in its reduced-assurance mode for the local-delegated profile.
Compensating controls are: (1) human-in-the-loop consent at delegation
time (FIDO2 / WebAuthn phishing-resistant authn), (2) short-lifetime
delegated access tokens (≤ 15 minutes) and even shorter `Txn-Token`s (≤ 60
seconds) bounding the per-call exploitation window, (3) per-issuance
peer verification at the WIB binding the agent identity to a code-signed
binary, and (4) continuous PDP evaluation on every `Txn-Token` issuance.
The AS reflects the achieved attestation depth in policy via the SVID’s
attest_methods claim (Section 5.3.2).
</aside>

## Authorization Server Endpoint Surface {#authorization-server-endpoint-surface}

The Authorization Server in this architecture exposes
three endpoints. Two are normative OAuth endpoints; one is defined by an
emerging Internet-Draft. This section describes the endpoint surface and
its standards posture; the detailed flows realized at each endpoint are
specified in Sections 5.2.2, 6.1, 7.1, and 7.3.

### /authorize: OAuth Authorization Endpoint (Normative) {#authorize-oauth-authorization-endpoint-normative}

Defined normatively by RFC 6749 Section 3.1. In this
architecture, the /authorize endpoint is used for the
standing-delegation consent ceremony, in which the Subject authorizes a
specific agent to act on their behalf for a defined scope.
Authentication of the Subject is performed at the IdP (Section 6.1) and
federated to the AS via OIDC; the /authorize endpoint itself records the
authorization decision, not the authentication. The granted
authorization is persisted as standing delegation policy that the AS
consults at the `/token` endpoint when minting delegated access tokens for
the agent. PKCE {{RFC7636}} applies per {{OAUTH-v2.1}} and {{RFC9700}}.
Phishing-resistant authentication via WebAuthn {{WebAuthn-L3}} is
REQUIRED.

### `/token`: OAuth Token Endpoint (Normative) {#token-oauth-token-endpoint-normative}

Defined normatively by RFC 6749 Section 3.2 and RFC
8693 (Token Exchange). The delegation grant flow detailed in Section 7.1
is realized at this endpoint, with
grant\_type=urn:ietf:params:oauth:grant-type:token-exchange. The AS
validates the Subject’s federated access token (issued by the IdP), the
WIB-issued JWT-SVID provided as the actor\_token (Section 5.2.3), and
the requested scope against the standing delegation policy from
/authorize. On success, it issues a delegated access token with sub set
to the Subject’s identifier and act set to the agent’s SPIFFE
identifier. This endpoint is invoked at the start of each agent task
that requires fresh delegated authority.

### `/txn-token`: Transaction Token Endpoint (Emerging) {#txn-token-transaction-token-endpoint-emerging}

Defined by {{OAUTH-TXN-TOKENS}}
(draft-ietf-oauth-transaction-tokens-08) and extended for AI agent
contexts by {{OAUTH-TXN-AGENTS}}
(draft-oauth-transaction-tokens-for-agents-00). Both are Internet-Drafts
in active development as of April 2026. The endpoint name, grant\_type
identifier, and request / response envelope are subject to change. The
`Txn-Token` issuance flow detailed in Section 7.3 is realized at this
endpoint. Implementations SHOULD track the current draft revisions and
treat this endpoint as unstable.

### Endpoint Co-location {#endpoint-co-location}

This document treats the AS, TTS, and embedded PDP role
as a single trust authority. Implementations MAY deploy them as separate
services or as a single service exposing the three endpoint paths above.
The trust bundle of enrolled WIB device keys (Section 5.2.2) MUST be
consistent across all three endpoints. Where a separately-deployed TTS
is used, it MUST share the AS’s trust bundle and standing delegation
policy store.

## AIMS Function-to-Section Mapping {#aims-function-to-section-mapping}

The seven AIMS functions, as defined in {{NIST-AIMS}}
and {{AI-AUTH}}, are realized in this document as follows. The
right-hand column lists the protocol or specification that supplies the
wire-level mechanics; this document supplies the
local-delegated-specific composition and the normative requirements that
bind the parts together.


| AIMS Function | Realization in this document | Underlying mechanism |
|---|---|---|
| Identifier | Section 5.3: SPIFFE ID assigned per agent instance, encoded as the sub claim of the WIB-issued JWT-SVID and propagated as the `act.sub` of the delegated access token. | [SPIFFE], [WIMSE-IDENTIFIER] |
| Credentials | Section 5.3.2: JWT-SVID minted by the WIB, signed with the WIB's enrolled device key. Lifetime ≤ 10 minutes. Section 7.1 delegated AT minted by AS, lifetime ≤ 15 minutes. Section 7.3 `Txn-Token`, lifetime ≤ 60 seconds. | [WIMSE-CREDS], [RFC9068], [OAUTH-TXN-TOKENS] |
| Attestation | Section 5.2.4: OS-level peer-process verification performed by the WIB on every issuance, six-step flow with platform-specific realization. Outcome reflected in the attest_methods SVID claim. | [OS-Workload-Attestation] §4 |
| Provisioning | Section 5.2.3: Workload API (FetchJWTSVID) over a host-only IPC channel, single-shot or long-lived-with-revalidation connection model. JIT issuance per agent task; no pre-minting. | [OS-Workload-Attestation] §3 |
| Authentication | Section 6.1: human Subject authenticates to the IdP via WebAuthn / FIDO2 (AAL2 minimum, AAL3 with hardware-attested device-bound passkey). Section 6.2: agent authenticates to the AS via OAuth 2.0 Token Exchange presenting the WIB-issued SVID as actor_token; the SVID itself is the proof of agent identity. | [WebAuthn-L3], [FIDO2-CTAP], [RFC8693], [NIST-63-4] |
| Authorization | Section 7.1: delegated access token with mandatory scope attenuation and sub / act split. Section 7.3: per-call `Txn-Token` carrying immutable identity and intent context. Section 7.4: intent binding via SHA-256 of user-declared task. PDP evaluation per Section 4.5. | [RFC8693], [OAUTH-TXN-TOKENS], [OAUTH-TXN-AGENTS] |
| Monitoring | Section 8: audit emissions at each PEP keyed on standard JWT identifiers (the AT's jti and the `Txn-Token`'s txn), revocation propagation, and CAEP-based real-time signaling. | [CAEP], this document §8 |

The mapping above is the contract this reference
architecture keeps with the AIMS model. An implementation that omits any
row MUST NOT claim conformance to this profile, regardless of the
strength of the remaining rows; the AIMS model treats the seven
functions as jointly necessary.

## Policy Decision Point (PDP) {#policy-decision-point-pdp}

The Policy Decision Point is an architectural role per
{{NIST-207}} and a first-class component of the AIMS Authorization
function per {{AI-AUTH}} Section 4. This section makes the PDP’s
presence and operation explicit, separately from the architecture’s
component inventory, because the document treats authorization as the
function under which the most policy decisions are made and the function
for which the cleanest existing-spec mapping exists.

In this reference architecture, the PDP is realized as
policy evaluation embedded within the AS’s `/token` and `/txn-token`
endpoints rather than as a separately-deployed service. There are two
PDP evaluation points, each with distinct inputs and a distinct decision
class:

- Per-task PDP evaluation at `/token`.
  Inputs: the Subject’s federated access token
  (sub, scopes, audience), the WIB-issued JWT-SVID and its
  attest\_methods claim (the AIMS Attestation evidence; see Section
  5.3.2), the standing delegation policy recorded at /authorize for this
  (Subject, agent) pair, and the requested scope. Decision: whether to
  mint a delegated access token, and at what scope (always a strict
  subset of the Subject’s scope per Section 7.1’s mandatory attenuation
  requirement). The per-task PDP MAY apply graduated trust based on
  attest\_methods. For example, it MAY refuse high-sensitivity scopes
  for SVIDs whose attest\_methods array does not include
  hardware-attested binary identity.
- Per-call PDP evaluation at `/txn-token`.
  Inputs: the previously-minted delegated access
  token (sub, act, scope), the agent-supplied intent\_hash (Section
  7.4), the agent-supplied tool\_call descriptor, and runtime context
  signals available at the trust authority (recent revocation events,
  anomaly signals, time-of-day risk factors per deployment policy).
  Decision: whether to mint a `Txn-Token` for this specific upstream
  invocation, and which intent context to bind into its tctx
  claim.

The PDP is the surface at which deployment-specific
policy lives. This document does not specify policy content; it
specifies the PDP’s position in the architecture, its inputs, and the
standard claim surfaces it consults. Implementers SHOULD consult
{{NIST-207}} for the underlying Zero Trust framing, {{AI-AUTH}} for the
agent-specific PDP role definition, {{CAEP}} for the input channel that
delivers real-time revocation events to the per-call PDP, and
{{OAUTH-TXN-TOKENS}} / {{OAUTH-TXN-AGENTS}} for the wire format the
per-call PDP’s decision is rendered into.

The PDP is NOT a separately-deployed service in this
architecture, but the role MAY be externalized if a deployment chooses
to do so. An externalized PDP would be consulted synchronously by the AS
during `/token` and `/txn-token` request handling. The wire format for that
consultation is out of scope for this document; implementations doing
this SHOULD use a recognized policy-evaluation transport such as those
discussed in {{NIST-207}}.

# Identification {#identification}

This section specifies the identifiers and
identity-issuance mechanisms used in the local delegated agent
architecture. It is the realization of four AIMS functions for the
local-delegated profile: Identifier (Section 5.3), Credentials (Section
5.3.2), Attestation (Section 5.2.4, by reference to
{{OS-Workload-Attestation}} Section 4), and Provisioning (Section 5.2.3,
by reference to {{OS-Workload-Attestation}} Section 3). Three classes of
identifier are defined: the Human Subject Identifier (Section 5.1), the
Agent Workload Identifier (Section 5.3), and the Delegation Relationship
Identifier (Section 5.4). Section 5.2 specifies the Workload Identity
Broker (WIB), the architectural component that solves the central
challenge of issuing verifiable identities to agent workloads running on
unattested end-user hardware.

## Human Subject Identifier {#human-subject-identifier}

The Human Subject Identifier is the IdP-issued sub
claim that names the human user. Its format is determined by the IdP and
is outside the scope of this document; typical values include opaque
user UUIDs, email addresses, or directory-service identifiers. The
Subject Identifier appears as the sub claim of the IdP-issued ID token
(Section 6.1), as the sub claim of the delegated access token issued by
the AS at `/token` (Section 7.1), and as the principal claim of the
`Txn-Token` issued at `/txn-token` (Section 7.3).

## Workload Identity Broker (WIB) {#workload-identity-broker-wib}

### Role and Trust Model {#role-and-trust-model}

The Workload Identity Broker (WIB) is the
locally-resident trust anchor that brokers agent workload identity on
unattested end-user devices. In AIMS terms, the WIB is the component
that realizes the Attestation function (by performing OS-level
peer-process verification on every issuance) and the Provisioning
function (by issuing JIT credentials only after Attestation has
succeeded for the requesting peer). Without the WIB, the local-delegated
profile has no AIMS-compliant Attestation surface; with it, the chain of
trust is anchored in OS code-signing rather than hardware-rooted
attestation.

The WIB pattern addresses the binary attestation gap
(see Gap G-7, Section 10.4) not by providing hardware-rooted attestation,
which is unavailable on consumer hardware, but by consolidating local
trust in a single hardened, code-signed daemon that issues short-lived
workload identities only to authenticated callers.

The Workload Identity Broker is an architectural role
that may be realized differently across deployment models. In this
document (local delegated), the WIB is realized as a code-signed
application running on the Subject’s device, and the verification
primitive is OS-level code signing checked against an allowlist (Section
5.2.4). In the companion remote delegated document, the WIB role is
fulfilled by the AS itself via workload identity federation with the
agent’s cloud-platform identity issuer; the verification primitive is
cryptographic validation of platform-issued workload tokens rather than
local code-signing. Across both deployments the WIB is the AIMS
Attestation realization; the platform-specific verification mechanism
differs.

In practice, the WIB is realized as an existing
user-trusted application on the device (typically a credential
management product) extended to broker workload identities. The
specification is vendor-neutral; conforming implementations may be
provided by any vendor whose application meets the requirements of this
section.

The WIB MUST satisfy the following requirements:

- Be a code-signed application, distributed and signed
  by a recognized vendor, and notarized by the host platform where
  applicable.
- Hold a device-bound asymmetric key pair generated in
  the platform secure key store (Apple Secure Enclave, Windows TPM, or
  equivalent). The private key MUST NOT leave the secure
  store.
- Be enrolled with the AS at install time (Section
  5.2.2). The AS MUST hold the WIB’s device public key in its trust
  bundle.
- Expose a Workload API (Section 5.2.3) on a host-only
  IPC channel.
- Verify the code-signing identity and bundle / product
  identity of every connecting agent process per
  {{OS-Workload-Attestation}} Section 4 before issuing any
  credential.
- Issue short-lived JWT-SVIDs ({{SPIFFE}},
  {{WIMSE-CREDS}}) to verified agent callers, signed with its enrolled
  device key.

The trust model is: the AS trusts the WIB (via
enrollment); the WIB trusts the OS code-signing subsystem to verify the
calling process’s binary identity; the agent inherits a verifiable
identity by presenting a WIB-issued SVID. To impersonate a verified
agent, an attacker MUST either compromise the OS code-signing subsystem,
subvert the WIB’s allowlist population channel, or compromise the WIB
itself, each of which is substantially harder than executing a process
under the same OS user account. The residual gap is enumerated in Gap
G-7.

### WIB Enrollment with the AS {#wib-enrollment-with-the-as}

The WIB MUST enroll its device-bound public key with
the AS prior to issuing any agent SVID. Enrollment establishes the WIB
as a recognized credential authority within the trust domain. Two
enrollment tiers are defined; a conforming implementation MUST realize
at least one. The enrollment ceremony is performed at the AS’s
/authorize endpoint (Section 4.3.1), with the AS recording the result as
an enrolled-WIB entry in its trust bundle.

Tier 1: Managed-Device Enrollment.
REQUIRED for enterprise deployments. The WIB
generates a key pair in the platform secure key store with platform
attestation (Apple Managed Device Attestation, Microsoft TPM
Attestation, or equivalent). The platform attestation is conveyed to the
AS as RATS evidence per {{RATS-ARCH}}. Enrollment is performed via the
enterprise IdP / MDM channel, which authorizes the device. Dynamic
Client Registration {{RFC7591}} is the wire format. The AS records the
WIB’s public key, device identifier, and binding to the enterprise
tenant.

Tier 2: User-Anchored Enrollment.
REQUIRED for consumer / unmanaged-device
deployments. The WIB generates a key pair in the platform secure key
store. Enrollment is anchored by a user WebAuthn ceremony
{{WebAuthn-L3}}: the user authenticates to the AS at /authorize with a
phishing-resistant credential, and within that ceremony the WIB’s public
key and any available device-binding evidence are conveyed and signed
under the user’s authorization. The AS records the WIB’s public key
bound to the authenticating user’s identity. Tier 2 carries lower
assurance than Tier 1 because platform attestation may be unavailable or
self-asserted; the AS MUST apply additional policy controls (e.g.,
shorter SVID lifetimes, stricter scope ceilings, more frequent
re-attestation) to Tier 2 enrollments.

After enrollment, the AS publishes the WIB’s public key
in its trust bundle, addressable by a WIB identifier of the form:

   
`wib://<vendor>/device/<device-uuid>`

The trust bundle is consulted at `/token` and `/txn-token`
whenever an SVID is presented as actor\_token.

### WIB-to-Agent Workload API (Provisioning) {#wib-to-agent-workload-api-provisioning}

The Workload API is the realization of the AIMS
Provisioning function for this profile: dynamic, just-in-time credential
issuance keyed on the runtime identity of the requesting workload. The
WIB exposes a Workload API to local agents that follows the patterns of
{{SPIFFE}} and {{WIMSE-CREDS}} over a host-only IPC channel. The
protocol is specified in full in {{OS-Workload-Attestation}} Section 3,
which defines:

- Supported request types (FetchJWTSVID required;
  FetchJWTBundles optional; FetchX509SVID not supported in this
  architecture).
- Per-platform IPC transport bindings: macOS XPC
  services and Unix domain sockets, Windows named pipes with
  same-session DACL pinning, Linux abstract-namespace sockets with
  kernel-atomic name claiming, and browser-sandbox native
  messaging.
- A user-gesture extension for high-sensitivity SPIFFE
  IDs, with cadence rules differentiated by agent\_class (every-issuance
  gesture for ai\_agent; bounded re-prompt window for
  developer\_tool).
- A closed-namespace error model and two-tier rate
  limiting (per-source pre-verification limit; per-verified-peer
  post-verification limit).
- The complete issuance flow including allowlist-miss
  handling and a separate first-run onboarding path
  (RegisterPeer).

The wire schema for the FetchJWTSVID request and
response, and for all error codes, is provided in
{{OS-Workload-Attestation}} Appendix A.

The provisioning surface is intentionally narrow: there
is no offline mode, no batch issuance, and no pre-mint pathway. Every
credential the agent obtains is the result of a fresh request that has
cleared the Attestation function (Section 5.2.4) for the specific agent
process making the request. This is the AIMS Provisioning property that
distinguishes agent identity from traditional pre-provisioned machine
identity.

### Local Process Verification (Attestation) {#local-process-verification-attestation}

Local Process Verification is the realization of the
AIMS Attestation function for the local-delegated profile. It is the
OS-level peer-credential authentication protocol that the WIB performs
on every Workload API connection before issuing any JWT-SVID. It
addresses the residual binary-attestation gap on consumer hardware (Gap
G-7) by anchoring the chain of trust in OS code-signing rather than
hardware-rooted attestation. The protocol is specified in full in
{{OS-Workload-Attestation}} Section 4, which defines:

- The threat model (T-1 through T-8) covering
  same-user-account adversaries, code-signing-subsystem subversions,
  allowlist-channel poisoning, and remote-filesystem TOCTOU.
- The six-step verification flow performed in order on
  every issuance request: (1) capture peer identity, (2) verify code
  signature against a pinned designated requirement, (3) verify runtime
  flags and entitlements, (4) verify post-launch instrumentation
  (RECOMMENDED), (5) verify launch context, and (6) verify peer
  ownership and freshness.
- Platform-specific normative realizations for macOS
  (audit\_token + pidversion + Code Signing API), Windows (named-pipe +
  CompareObjectHandles + WinVerifyTrust), Linux (abstract sockets +
  pidfd or ucred + IMA where available), and browser-sandbox agents
  (native messaging host with two-layer trust binding).
- The allowlist schema, including the agent\_class
  property that distinguishes developer\_tool from ai\_agent and the
  policy consequences of that distinction.
- Verification-cadence rules for single-shot and
  long-lived-with-revalidation connection models, including the
  conditions under which Steps 2 to 5 may be elided on the steady-state
  path.

The Attestation function’s outcome (which methods
succeeded, which mechanisms were used) is reflected in the SVID’s
attest\_methods claim per Section 5.3.2 of this document, so the AS can
apply graduated trust based on the achieved verification depth. This
reflection is what makes the AIMS Attestation function useful to the
downstream Authorization function: the AS does not need to trust the
WIB’s self-rating of assurance; it sees the per-issuance evidence and
applies policy accordingly.

<figure anchor="fig-2">
<name>Figure 2</name>
<artwork type="ascii-art" align="center">
@@IMG:assets/images/local-delegated/image2.png@@
</artwork>
</figure>

Sequence 5.1: WIB-mediated
agent identity issuance plus Token Exchange. The six-step verification
of {{OS-Workload-Attestation}} §4 (AIMS Attestation) precedes JWT-SVID
minting (AIMS Credentials, AIMS Provisioning); the SVID is then
presented as actor\_token in the AS Token Exchange (AIMS Authentication,
agent leg).

## Agent Workload Identifier: AIMS Identifier {#agent-workload-identifier-aims-identifier}

Section 5.3 realizes the AIMS Identifier function. The
identifier scheme is SPIFFE {{SPIFFE}}, chosen because it is
URI-formatted, hierarchically structured, and already integrated with
the WIMSE family of workload-identity specifications referenced
throughout this document.

### SPIFFE ID Format {#spiffe-id-format}

Each agent workload instance MUST be assigned a SPIFFE
ID per {{WIMSE-IDENTIFIER}} and {{SPIFFE}}. The identifier takes URI
form:

~~~
spiffe://<trust-domain>/agent/<vendor>/<agent-type>/<instance-id>
~~~

Example (native local process):

~~~
spiffe://acme.com/agent/example-vendor/example-agent/8f3a2b1c-9d4e-11ec-b909-0242ac120002
~~~

Example (browser-sandbox, origin-scoped):

~~~
spiffe://acme.com/agent/<vendor>/browser-ext/<origin-hash>/<session-id>
~~~

The `<vendor>` segment MUST identify the agent’s
publisher and is bound to the code-signing identity verified by the WIB
(Section 5.2.4). The `<agent-type>` segment identifies the product.
The `<instance-id>` MUST be a UUIDv4 generated fresh at agent
instantiation; it MUST NOT be reused across sessions.

For browser-sandbox agents, the trust domain MUST
reflect the registered origin of the web application, preventing
cross-origin impersonation.

The SPIFFE ID is the sub claim of the WIB-issued SVID
and is propagated as the `act.sub` claim in the delegated access token
issued by the AS at `/token` (Section 7.1).

### WIB-Issued SVID Claims: AIMS Credentials {#wib-issued-svid-claims-aims-credentials}

Section 5.3.2 realizes the AIMS Credentials function
for the agent-identity leg of the trust chain. The credential format is
JWT-SVID per {{WIMSE-CREDS}}; the AS-issued delegated access token
(Section 7.1) and the TTS-issued `Txn-Token` (Section 7.3) are the further
AIMS credentials produced downstream of this one.

The SVID minted by the WIB is a JWT signed with the
WIB’s enrolled device key. Example claim body:


~~~
{
  "iss":
  "wib://<vendor>/device/<device-uuid>",
  "sub":
  "spiffe://<trust-domain>/agent/<vendor>/<agent-type>/<instance-id>",
  "aud": "https://as.acme.com",
  "iat": 1745000000,
  "exp": 1745000600,
  "jti": "9f8e7d6c-...",
  "bound_subject":
  "user:7f3a2b1c@acme.com",
  "attest_methods": ["macos_codesign", "secure_enclave_devid", "user_gesture"],
  "binary_id": {
    "publisher":
    "<team-id-or-publisher>",
    "product_id":
    "<bundle-or-product-id>",
    "cdhash": "sha256:..."
  }
}
~~~
Claim semantics:

- iss: identifies the issuing
  WIB by the identifier registered at enrollment (Section 5.2.2).
- sub: the agent’s SPIFFE ID
  per Section 5.3.1.
- aud: the AS endpoint
  URL.
- jti: a unique identifier for
  this SVID, used by the AS for replay detection over the SVID’s
  lifetime and as one of the audit correlation handles consumed by AIMS
  Monitoring (Section 8).
- bound\_subject: the OS-level
  user identifier the agent is bound to. The AS MUST verify that
  bound\_subject matches the sub of the Subject’s federated access token
  in the `/token` exchange.
- attest\_methods: an array
  enumerating the verification methods that succeeded for this SVID
  issuance. This is the wire-level reflection of the AIMS Attestation
  outcome per Section 5.2.4. The AS MAY apply graduated trust based on
  this array (e.g., requiring secure\_enclave\_devid for
  production-resource scopes, or rejecting SVIDs that contain only
  user\_gesture for high-sensitivity audiences).
- binary\_id: structured
  representation of the verified binary identity. Used for audit logging
  (AIMS Monitoring, Section 8) and policy evaluation at the AS.

SVID lifetime MUST NOT exceed 10 minutes and MUST NOT
exceed the lifetime of any access token derived from it. Short lifetime
is not optional: it is the AIMS Credentials property that bounds the
blast radius of credential theft to the residual TTL plus the time
required for revocation propagation per Section 8.3.

## Delegation Correlation {#delegation-correlation}

Audit logs and revocation operations need to associate
an observed agent action with the specific delegation event that
authorized it. This document achieves correlation using only standard
JWT claims, specifically the access token’s jti and the `Txn-Token`’s txn,
rather than introducing a vendor-specific delegation identifier. The
pair (AT.jti, txn) uniquely identifies a single agent action within a
single delegated task across all PEPs that observe it.

The AS MUST set a fresh jti on every delegated access
token issued at `/token` (Section 7.1). The TTS MUST set a fresh txn on
every `Txn-Token` issued at `/txn-token` (Section 7.3) and MUST include the
originating AT’s jti as an additional correlation claim in the `Txn-Token`
(the `Txn-Token` specification calls out this propagation pattern in
{{OAUTH-TXN-TOKENS}} and {{OAUTH-TXN-AGENTS}}). PEPs that admit a
request MUST log both identifiers per Section 8.1.

Earlier drafts of this document defined a custom
dlg\_id claim to anchor delegations explicitly. That mechanism is
deferred to separate work (Section 12) where it can be defined as a
complete specification rather than a paragraph in a profile document.
Until then, the standard jti / txn pairing is sufficient for the
correlation needs of this profile.

# Authentication (AuthN) {#authentication-authn}

This section realizes the AIMS Authentication function.
AIMS Authentication has two legs in the local-delegated profile: (a) the
human Subject’s authentication to the IdP at delegation time (Section
6.1), and (b) the agent workload’s authentication to the AS at task time
(Section 6.2). Both legs feed evidence into the downstream Authorization
function (Section 7); neither alone is sufficient. The agent leg
additionally consumes the AIMS Attestation output (Section 5.2.4) as the
actor\_token presented in Token Exchange.

## Human-to-IdP Authentication {#human-to-idp-authentication}

The Subject MUST authenticate to the IdP using a
phishing-resistant method prior to any delegation. Per {{NIST-63-4}}
(finalized July 2025), the MINIMUM assurance level for delegating
authority is AAL2. Synced passkeys satisfy AAL2;
device-bound passkeys with hardware attestation satisfy AAL3.

The RECOMMENDED flow for local agent environments
is:

- Subject navigates to the agent’s authorization
  endpoint (or the agent triggers the OS browser to open the IdP
  authorization URL).
- IdP presents a WebAuthn {{WebAuthn-L3}} challenge.
  The Subject authenticates using a device-bound passkey (TPM-backed on
  Windows / macOS via Windows Hello / Secure Enclave) or a FIDO2
  hardware security key ({{FIDO2-CTAP}}).
- WebAuthn assertion is verified by the IdP. On
  success, the IdP issues an authorization code.
- The agent’s OAuth client (a public client, per
  {{RFC6749}} Section 2.1) exchanges the code for an ID token and access
  token, using PKCE {{RFC7636}} to prevent code interception.

The Subject AT obtained at the conclusion of the OAuth
Authorization Code flow is held by the OAuth client component that
completed the flow. For the agent to present this AT as subject\_token
in the Token Exchange of §7.1, it MUST be delivered from the OAuth
client component to the agent’s credential-handling layer (§7.5.1) over
a channel that does not expose it to other same-user processes beyond
what the OS already permits, and that does not expose it to the LLM
context. The specific delivery mechanism depends on the agent’s
deployment shape: native CLI agents typically use a loopback redirect
URI {{RFC8252}}, with the OAuth client’s redirect\_uri pointing at a
localhost port the agent is bound to; native desktop agents typically
use a custom URL scheme or platform-specific deep-link mechanism;
browser-extension agents already operate in the same origin context as
the OAuth client and complete the flow without a cross-process handoff;
and IDE-integrated agents use the IDE’s secure-storage API or extension
messaging surface. In all cases, the AT is consumed once by the agent
(presented as subject\_token to the AS at `/token`, after which the agent
holds only the delegated AT, not the Subject AT) and SHOULD be discarded
from the OAuth client component after handoff. The AT is short-lived per
the IdP’s policy; this specification does not constrain its lifetime,
only the delivery property.

PKCE is REQUIRED for all local agent OAuth flows per
{{OAUTH-v2.1}} and {{RFC9700}} Section 2.1.1.

<figure anchor="fig-4">
<name>Figure 4</name>
<artwork type="ascii-art" align="center">
@@IMG:assets/images/local-delegated/image4.png@@
</artwork>
</figure>

Sequence 6.1: Human authentication to IdP via FIDO2 +
OAuth PKCE auth code flow. This realizes the human leg of AIMS
Authentication. The Subject AT issued at the end of this flow becomes
the subject\_token for the agent Token Exchange in Section 7.1.

## Agent-to-AS Authentication {#agent-to-as-authentication}

After the human Subject authenticates, the agent
obtains its own short-lived credential through a Token Exchange
{{RFC8693}}, detailed in Section 7.1. This is the agent leg of AIMS
Authentication.

The agent’s actor\_token in this exchange is a JWT-SVID
issued by the Workload Identity Broker (Section 5.2.3), not a
self-asserted JWT; the AS validates the SVID’s signature against its
enrolled-WIB trust bundle (Section 5.2.2) before processing the
exchange. The SVID itself is the proof of agent identity. It was minted
only after the WIB performed the six-step verification of
{{OS-Workload-Attestation}} Section 4 against the connecting agent
process and signed the result with the WIB’s device-bound key from the
platform secure key store. From the AS’s perspective, accepting a
WIB-issued SVID is equivalent to accepting an attestation that the WIB
has verified the agent’s binary identity, runtime integrity, launch
context, and ownership.

Token Exchange itself is a public-client OAuth flow per
{{RFC6749}} Section 2.1 and uses the subject\_token + actor\_token grant
of {{RFC8693}}. The agent does not hold a long-lived asymmetric key for
client authentication and is not required to demonstrate
proof-of-possession on the Token Exchange request itself; the
actor\_token (the WIB-issued SVID) carries the agent identity, and the
SVID’s short lifetime, audience binding, bound\_subject claim, and
per-issuance attestation evidence collectively bound the trust placed in
it.

Note on proof-of-possession on the issued AT.
The delegated access token issued at `/token` is a
bearer token in this revision. Per-call proof-of-possession is provided
by the `Txn-Token` (Section 7.3), which is short-lived (≤ 60 seconds),
carries an immutable identity and intent context, and is independently
issued by the TTS for each upstream invocation. Proof-of-possession on
the AT itself, by DPoP, mTLS, or another mechanism, is deferred to
separate work; see Section 12.

## Agent Credential Lifecycle {#agent-credential-lifecycle}

Agent credentials MUST be ephemeral. The following
REQUIRED constraints apply, all of which derive from the AIMS
Credentials property that an agent identity is bounded in time and scope
to a single delegated task:

- WIB-issued SVIDs MUST have a maximum lifetime of 10
  minutes.
- Agent delegated access tokens MUST have a maximum
  lifetime of 15 minutes.
- `Txn-Token`s (Section 7.3) MUST have a maximum lifetime
  of 60 seconds per {{OAUTH-TXN-TOKENS}}.
- Refresh tokens MUST NOT be issued to local agent
  clients for agent-scoped access tokens. If the access token expires
  mid-task, the agent MUST request a fresh delegation through the WIB’s
  Workload API (which will trigger fresh peer verification per
  {{OS-Workload-Attestation}} §4) and a fresh `/token` exchange. The
  absence of refresh tokens is itself an AIMS property: continuity of
  authority across time is a Subject decision, not an agent
  capability.
- The agent process does not hold long-lived asymmetric
  key material in this profile. The WIB holds a device-bound key in the
  platform secure key store; the agent presents WIB-issued SVIDs (which
  the WIB has signed for it) and AS-issued bearer tokens, neither of
  which the agent itself signs.

# Authorization (AuthZ) {#authorization-authz}

This section realizes the AIMS Authorization function.
AIMS Authorization in this profile operates at two granularities: (a)
per-task, at the AS’s `/token` endpoint (Section 7.1), where a delegated
access token is minted with a scope-attenuated authorization derived
from the Subject’s standing delegation policy and the Attestation
outcome carried in the SVID; and (b) per-call, at the AS’s `/txn-token`
endpoint (Section 7.3), where a `Txn-Token` is minted carrying immutable
identity and intent context for a specific upstream invocation. Both
granularities are required: the per-task layer bounds what the agent
could do; the per-call layer bounds what the agent does do, and is the
surface that the AIMS Monitoring function (Section 8) observes. The
Policy Decision Point (Section 4.5) evaluates inputs at both
granularities.

## Delegation Grant Flow {#delegation-grant-flow}

The core of the delegated authority model is the Token
Exchange {{RFC8693}} that converts the Subject’s access token into an
agent-scoped delegated access token carrying both the Subject’s identity
(sub claim) and the agent’s identity (act claim). This is the AIMS
Authorization function operating at per-task granularity.

Token Exchange Request parameters:


~~~
POST /token
Content-Type: application/x-www-form-urlencoded

grant_type=urn:ietf:params:oauth:grant-type:token-exchange
&subject_token=<subject-access-token>
&subject_token_type=urn:ietf:params:oauth:token-type:access_token
&requested_token_type=urn:ietf:params:oauth:token-type:access_token
&audience=https://api.example.com
&scope=resource:dataset-id:read     # MUST be subset of subject's scopes
&actor_token=<wib-issued-jwt-svid>
&actor_token_type=urn:ietf:params:oauth:token-type:jwt
~~~

The AS MUST:

- Validate the subject\_token (signature, expiry,
  audience).
- Validate the actor\_token: verify that the WIB-issued
  JWT-SVID (Section 5.2.3) is signed by a key in the AS’s enrolled-WIB
  trust bundle (Section 5.2.2), and that the SVID’s bound\_subject claim
  matches the subject\_token’s sub. Inspect the SVID’s attest\_methods
  claim (the AIMS Attestation reflection) and apply graduated-trust
  policy per Section 5.3.2 and Section 4.5.
- Verify that the requested scope is a strict subset of
  the subject\_token’s scopes (mandatory scope attenuation).
- Set sub to the Subject’s identifier and act to the
  agent’s WIMSE identifier.
- Set a fresh jti on the issued token for replay
  detection and audit correlation (Section 5.4).
- Set exp no more than 15 minutes from issuance.

Example delegated access token claims (JWT body):

~~~
{
   "iss": "https://as.acme.com",
   "sub": "user:7f3a2b1c@acme.com",
   "act": {
     "sub": "spiffe://acme.com/agent/example-vendor/example-agent/8f3a2b1c..."
   },
   "aud": "https://api.example.com",
   "scope": "resource:dataset-id:read",
   "jti": "a4f8c1b2-0c4e-11ed-b939-0242ac120002",
   "exp": 1745000000,
   "iat": 1744999100
}
~~~

<aside markdown="1">
**SECURITY GAP**

Gap G-2: Scope Attenuation in RFC 8693.
RFC 8693 does not mandate scope attenuation: it
allows the resulting token to have the same or broader scopes than the
`subject_token`. In typical delegation scenarios, the Subject may hold
broad access across many resources, but the agent MUST be issued a token
scoped only to the specific resource and operation it requires (e.g., a
single dataset with read-only access). Implementations MUST explicitly
enforce that the delegated token’s scope is a strict subset of the
subject token’s scope. This is the AIMS Authorization principle of least
privilege; without scope attenuation enforcement, this profile does not
satisfy AIMS Authorization. The emerging
draft-sweeney-oauth-agent-delegation-00 (anticipated IETF 125) profiles
RFC 8693 to mandate this, along with chain verification and revocation
propagation. Until standardized, AS implementations MUST enforce
attenuation in local policy.
</aside>

## Resource Access Flow {#resource-access-flow}

Once the agent holds a
delegated access
token,
it presents this token to Resource Servers along with a per-call
`Txn-Token` (Section 7.3). Each request MUST include:

- An Authorization header bearing the delegated access
  token (Bearer scheme).
- A `Txn-Token` header (see Section 7.3) carrying the
  per-call transaction context, including the intent\_hash and
  tool\_call descriptor.

The Resource Server’s validation of these two artifacts
is the PEP leg of the AIMS Authorization function. The RS MUST validate
(a) the access token’s signature against the AS’s published JWKS, (b)
the access token’s audience matches the RS, (c) the access token has not
expired, (d) the `Txn-Token`’s signature against the TTS’s published JWKS,
(e) the `Txn-Token`’s short lifetime has not been exceeded, and (f) the
`Txn-Token`’s sub and `actor.sub` match the access token’s sub and `act.sub`.
The RS MUST then enforce the requested action against the granted scope
and emit a structured audit record per Section 8.1 on every
authorization decision (admit or deny), with the access token’s jti, the
`Txn-Token`’s txn, the `act.sub`, and the action as the primary correlation
keys.

Per-call sender-constraining of the access token (DPoP,
mTLS, or other proof-of-possession) is not specified in this revision.
The `Txn-Token`’s short 60-second lifetime, combined with the immutable
identity context it carries and the requirement that a fresh `Txn-Token`
be obtained from the TTS for each upstream invocation, bounds the
per-call replay window. The TTS’s refusal to mint a `Txn-Token` under a
revoked or expired access token (Section 8.3) provides the equivalent of
CAEP-mediated revocation propagation for the per-call layer. See Section
10 for the residual risk analysis and Section 12 for the deferred
AT-binding work.

<figure anchor="fig-3">
<name>Figure 3</name>
<artwork type="ascii-art" align="center">
@@IMG:assets/images/local-delegated/image3.png@@
</artwork>
</figure>

Sequence 7.2: Agent resource access. The agent obtains
a fresh `Txn-Token` from the TTS for each upstream invocation, then
presents the delegated AT and `Txn-Token` to the Resource Server. The PEP
validates both, enforces scope, and emits AIMS Monitoring audit records
keyed on at\_jti and txn.

## Transaction Token Propagation {#transaction-token-propagation}

Section 7.3 realizes the per-call leg of the AIMS
Authorization function. `Txn-Token`s per {{OAUTH-TXN-TOKENS}} provide
immutable identity and context propagation through the agent’s call
chain. The {{OAUTH-TXN-AGENTS}} extension adds actor (agent) and
principal (human) context fields specifically for AI agent
workloads.

`Txn-Token` Request from the local agent to the TTS:

~~~
POST /txn-token
Content-Type: application/x-www-form-urlencoded
Authorization: Bearer <delegated-AT>
grant_type=urn:ietf:params:oauth:grant-type:token-exchange

&requested_token_type=urn:ietf:params:oauth:token-type:txn_token
&subject_token=<delegated-AT>
&subject_token_type=urn:ietf:params:oauth:token-type:access_token
&audience=<trust-domain-name>
&request_details=<base64url(intent-context-json)>
&request_context=<base64url(runtime-context-json)>
~~~

The TTS MUST extract from the delegated AT:

- sub  → becomes the
  `Txn-Token`’s sub (human subject)
- `act.sub`  → becomes the
  `Txn-Token`’s actor context (agent WIMSE ID)
- jti  → preserved in the
  `Txn-Token` as the at\_jti claim for audit correlation (consumed by AIMS
  Monitoring, Section 8). The `Txn-Token` itself receives a fresh txn
  identifier per {{OAUTH-TXN-TOKENS}}.

Example `Txn-Token` claims:

~~~
  {
      "iss": "https://tts.acme.com",
      "iat": 1744999200,
      "exp": 1744999260,   // 60-second lifetime
      "txn": "txn:9a1b3c2d-...",
      "sub": "user:7f3a2b1c@acme.com",
      "aud": "https://api.example.com",
      "req_wl": "https://gateway.api.example.com",
      "actor": {
        "sub": "spiffe://acme.com/agent/example-vendor/example-agent/8f3a2b1c...",
        "type": "ai_agent"
      },
      "principal": {
        "sub": "user:7f3a2b1c@acme.com",
        "iss": "https://idp.acme.com"
      },
      "at_jti": "a4f8c1b2-0c4e-11ed-b939-0242ac120002",
      "tctx": {
        "intent_hash": "<sha256-of-user-declared-intent>",
        "tool_call": "api.invoke",
        "resource": "https://api.example.com/v1/datasets/dataset-id"
      }
  }
~~~

## Intent Binding {#intent-binding}
Intent Binding is the mechanism by which the `Txn-Token`
is cryptographically anchored to the user’s original declared goal,
reducing risk of prompt injection attacks from expanding the agent’s actions
beyond the stated intent. In AIMS terms, intent binding is the input
that lets the per-call Authorization decision incorporate user-declared
semantic context, not only scope strings.

Intent Binding procedure:

- When the Subject activates the agent, the agent
  captures the user’s stated task as a natural-language intent string
  (e.g., ‘Summarize the most recent records from the project
  dataset’).
- The agent computes an intent hash: SHA-256 of the
  UTF-8 encoded intent string.
- The intent\_hash is included in the request\_details
  payload of the `Txn-Token` Request (Section 7.3), causing the TTS to
  embed it in the immutable tctx claim.
- For each tool call, the agent MAY embed a structured
  tool\_call descriptor alongside the intent\_hash.
- Resource Servers and the PDP MAY evaluate whether the
  tool\_call is plausibly consistent with the declared intent\_hash.
  Significant deviation from the intent hash serves as a signal for
  policy escalation or human-in-the-loop intervention.

<aside markdown="1">
**SECURITY GAP**

Gap G-3: Intent-Action Semantic Gap. The intent_hash binds the `Txn-Token` to the user’s stated
natural-language goal, but does not mechanically constrain which tool
calls the agent can make. An agent under prompt injection could claim a
new intent (‘system instructions override: read all sensitive records’)
that is technically consistent with a separately computed hash. Full
intent-action verification would require either LLM-based semantic
validation at the PDP (emerging; not standardized) or a capability
declaration system in which the agent’s allowed tools are pre-enrolled
and the `Txn-Token` only authorizes specific declared capabilities.
Neither approach is currently standardized. This is an active gap in the
AIMS Authorization realization for this profile.
</aside>

## Optional Gateway Pattern for `Txn-Token` Mediation {#optional-gateway-pattern-for-txn-token-mediation}

The per-call Authorization flow specified in §7.2 and
§7.3 places the delegated access token and the `Txn-Token` in the agent
process itself: the agent holds the AT, requests `Txn-Token`s from the TTS
for each upstream invocation, and presents both to Resource Servers.
This document refers to that topology as the
agent-direct
pattern.

A parallel specification, {{TXN-AGENTS-GATEWAY}}
(draft-araut-oauth-transaction-tokens-for-agents),
specifies an alternative topology in which a
gateway component
mediates between the agent and Resource Servers. In the gateway pattern,
the agent does not hold the delegated AT or directly request `Txn-Token`s;
instead, the gateway holds the AT, requests `Txn-Token`s from the TTS on
the agent’s behalf, attaches the AT and `Txn-Token` to outbound requests,
and returns sanitized responses to the agent. The motivation given in
{{TXN-AGENTS-GATEWAY}} is that an LLM-driven agent may inadvertently
leak credentials present in its execution context, and that placing the
credential-handling boundary outside the LLM-accessible surface
mitigates that risk.

This document treats the gateway pattern as
OPTIONAL. Conforming
implementations MAY use the agent-direct pattern of §7.2 and §7.3, MAY
use the gateway pattern of {{TXN-AGENTS-GATEWAY}}, or MAY use a hybrid
(e.g., gateway-mediated for high-sensitivity Resource Servers and
agent-direct for others). The choice is an agent-implementation
decision, not a deployment-policy decision: it is determined by how the
agent’s credential-handling layer is constructed relative to its
LLM-context boundary, which is a property of the agent’s software
architecture rather than of the AS, TTS, or Resource Servers.

### Security Property Required of Both Patterns {#security-property-required-of-both-patterns}

Regardless of which pattern is chosen, conforming
implementations MUST satisfy the following property:

Credential isolation from LLM context. The
delegated access token, `Txn-Token`s, the Subject AT (during the brief
interval it is held by the agent host before Token Exchange), and the
WIB-issued JWT-SVID MUST NOT be placed in any input, output, system
prompt, tool result, retrieved document, or other content visible to the
LLM that drives the agent’s reasoning. Implementations MUST treat these
credentials as belonging to the agent’s credential-handling layer, not
to its reasoning layer.

This property is what the gateway pattern enforces
structurally (by removing the credentials from the agent process
entirely) and what the agent-direct pattern requires the agent’s
software architecture to enforce (by partitioning the agent process into
a credential-handling layer that holds tokens and a reasoning layer that
does not). Either approach is conformant; neither is conformant if the
property is violated.

The choice between patterns has trade-offs:

- Agent-direct. Lower latency
  (no extra hop), simpler deployment topology, fewer components to
  operate. Requires the agent author to architect the agent process such
  that the credential-handling code path is structurally separate from
  the LLM-context construction code path. Appropriate when the agent
  author controls the full agent codebase and can guarantee the
  partition.
- Gateway-mediated. Higher
  latency (extra hop on every Resource Server invocation), additional
  component to deploy and secure, but the credential-isolation property
  is enforced by process boundary rather than by software discipline.
  Appropriate when the agent is built on top of a third-party LLM
  framework whose context-construction behavior the agent author cannot
  fully audit, or when defense-in-depth against agent-internal
  credential leakage is required by deployment policy.

### Wire Differences When the Gateway is Used {#wire-differences-when-the-gateway-is-used}

When the gateway pattern is used, the wire-level
interactions differ from §7.2 and §7.3 as follows:

- The agent →
  gateway call carries the agent’s intent and
  tool descriptor (the same
  intent\_string and
  tool\_call envelope
  that §7.4 specifies the agent constructs) but does not carry the
  delegated AT or any `Txn-Token`. The transport from agent to gateway is
  implementation-defined and MUST be local to the agent’s host
  (typically a localhost-bound HTTP listener, a Unix domain socket, or
  an in-process function call); cross-host gateway topologies are out of
  scope for this revision because they cross a trust boundary that this
  document does not analyze.
- The gateway →
  TTS call is the
  `/txn-token` request
  specified in §7.3, with the gateway acting as the OAuth client. The
  gateway holds the delegated AT and presents it as
  subject\_token. The
  intent\_hash and tool\_call values are computed by the agent and
  conveyed to the gateway over the agent → gateway interface
  above.
- The gateway → Resource
  Server call is the resource invocation
  specified in §7.2, with the gateway attaching the delegated AT in the
  Authorization header
  and the `Txn-Token` in the
  `Txn-Token` header. The
  Resource Server’s PEP validation is unchanged from §7.2.
- The gateway →
  agent response carries only the sanitized
  Resource Server response. The gateway MUST NOT echo the AT, the
  `Txn-Token`, or any error detail that contains credential material back
  to the agent.

The Resource Server is unaware of which pattern is in
use. From the PEP’s perspective, the wire format and audit emission are
identical (§8.1). The
`act.sub` in the AT and
the `actor.sub` in the
`Txn-Token` continue to identify the agent (not the gateway); the gateway
is a credential-handling component, not a delegation participant.

### Gateway Threat Considerations {#gateway-threat-considerations}

A gateway introduces a component that holds delegated
access tokens for one or more agents. Implementations using the gateway
pattern MUST:

- Bind the gateway’s accepting interface to the agent’s
  process identity (on the same host) using the same OS-level
  peer-process verification that the WIB performs per
  {{OS-Workload-Attestation}} §4. A localhost-bound gateway that accepts
  requests from any same-user process is not conformant; an attacker
  process running as the same user could otherwise drive the gateway to
  issue `Txn-Token`s against an arbitrary delegated AT the gateway
  holds.
- Apply the same credential-storage requirements to the
  gateway’s AT cache that §10.4.1 applies to in-agent token storage
  (short-lived, OS-protected where available, zeroized on process
  termination).
- Emit audit records per §8.1 from the gateway, with
  the gateway’s identity recorded alongside the agent’s identity. The
  Subject-visible activity log of §8.5 MUST attribute actions to the
  agent, not to the gateway, because the gateway is not the delegation
  participant; the gateway’s involvement is a deployment-topology fact,
  not an authority fact.

### Implementation Guidance (Informative) {#implementation-guidance-informative}

Agent authors choosing between the two patterns should
consider where credential-handling code sits relative to the LLM context
construction in their architecture. If the agent process is structured
as a thin LLM-orchestration layer plus a separately-bounded
credential-handling subprocess (e.g., the credential-handling code runs
in a worker process or in a memory-isolated sandbox), the agent-direct
pattern is straightforwardly conformant. If the agent process is built
on a framework that constructs LLM context from broad reflection of the
agent’s state, the gateway pattern provides a stronger structural
guarantee.

Hybrid topologies are explicitly permitted: a
deployment may route invocations of a high-sensitivity Resource Server
through a gateway while invoking lower-sensitivity Resource Servers
agent-direct, choosing the trade-off per-resource. The Subject-visible
activity log MUST present a unified view across both topologies
(§8.5).

# Monitoring, Audit, and Revocation {#monitoring-audit-and-revocation}

This section realizes the AIMS Monitoring function.
AIMS Monitoring is the seventh and final function of the {{NIST-AIMS}} /
{{AI-AUTH}} model and the function that makes the other six accountable.
Without a per-action, correlatable, tamper-evident audit surface and a
real-time signal channel for policy events, the upstream Identifier,
Credentials, Attestation, Provisioning, Authentication, and
Authorization functions cannot be operated as a Zero Trust system: there
is no observation of whether they are doing what they are supposed to
do, and no mechanism to react when they are not. Earlier drafts of this
document folded monitoring concerns into other sections (a brief mention
in Section 5.4, the audit hint in Section 7.2, the revocation discussion
in Section 8.3); this revision consolidates them into a single
AIMS-aligned section. Correlation in this revision uses standard JWT
claims (the access token’s jti and the `Txn-Token`’s txn) rather than a
vendor-specific delegation identifier.

## Audit Emission Requirements {#audit-emission-requirements}

Every Policy Enforcement Point in the architecture
(every Resource Server, the AS, and the TTS) MUST emit a structured
audit record on every authorization-relevant event. The set of events is
closed; conforming implementations MUST emit at minimum the following
classes of record:

| Event class | Emitted by | Required correlation fields |
|---|---|---|
| Delegation issued | AS at /token | AT jti, sub, `act.sub`, scope, attest_methods, audience, exp |
| Delegation refused | AS at /token | sub, attempted `act.sub`, refusal reason class |
| `Txn-Token` issued | TTS at `/txn-token` | txn, at_jti, sub, `act.sub`, intent_hash, `tool_call`, resource |
| `Txn-Token` refused | TTS at `/txn-token` | at_jti (from presented AT), attempted action, refusal reason class |
| Resource access admitted | Resource Server PEP | txn, at_jti, sub, `act.sub`, resource, action |
| Resource access denied | Resource Server PEP | txn, at_jti, sub, `act.sub`, resource, action, deny reason class |
| WIB SVID issued | WIB | SVID jti, sub (SPIFFE), bound_subject, attest_methods, binary_id.cdhash, exp |
| WIB SVID refused | WIB | attempted sub, refusal reason class (per Appendix A.3 of [OS-Workload-Attestation]) |
| User-gesture surfaced | WIB | sub (SPIFFE), gesture mechanism, accepted / declined / unavailable |
| Token revoked | AS or upstream signal source | AT jti (or SVID jti for WIB-issued credentials), sub, `act.sub`, revocation reason class, propagation channel |

The refusal reason classes MUST be drawn from a closed
namespace, identical at each emission site, so that operators querying
audit data can compare across deployments. This document defines the
closed namespaces in Appendix B (forthcoming in -01); until then,
deployments MAY define their own provided the namespace is consistent
within the deployment and version-stamped on every record.

Audit records MUST NOT include verification-step diagnostic
detail beyond the closed-namespace reason class on emissions visible to
the requesting peer. Detailed step-level failure information MAY be
recorded in a separate, operator-only audit channel; this is the same
separation defined in {{OS-Workload-Attestation}} Section 3.4 for WIB
error responses, applied to the broader audit surface here.

## Correlation: at\_jti, txn, and the Identity Chain {#correlation-at-jti-txn-and-the-identity-chain}

The AIMS Monitoring function depends on being able to
reconstruct, from audit records alone, the full identity chain of any
observed action: which Subject, acting through which Agent, under which
delegated access token, in which Transaction, against which Resource.
The wire-level mechanism that makes this possible is the propagation of
two standard JWT identifiers through every layer of the
architecture:

- at\_jti: the access token’s
  jti claim, set by the AS at `/token` (Section 7.1) and copied into the
  `Txn-Token` by the TTS at `/txn-token` (Section 7.3) for cross-layer
  correlation. The at\_jti is the audit anchor for the per-task layer of
  AIMS Authorization.
- txn: the per-transaction
  identifier minted at `/txn-token` (Section 7.3). The txn is the audit
  anchor for the per-call layer.

The pair (at\_jti, txn) uniquely identifies a single
agent action within a single delegated task, across all PEPs that
observe it. PEPs MUST log both. Audit-store schemas SHOULD index on
at\_jti to support the operational query “show me everything done under
access token Y,” which is the canonical retrospective-investigation
query for a delegated agent system. Both identifiers are standard JWT
claims; no custom correlation field is required.

## Revocation and Real-Time Signaling {#revocation-and-real-time-signaling}

AIMS Monitoring is not only a backward-looking audit
function; it is also the input channel for forward-looking policy
reaction. When the Subject (or an automated risk system) determines that
an active delegation has been compromised or should be terminated, the
Monitoring surface is responsible for propagating that determination to
every component that holds outstanding authority. Because this revision
uses standard JWT claims rather than a custom delegation identifier,
revocation is keyed on the access token’s jti (and, where the entire
(Subject, agent) relationship is being revoked, on the standing
delegation policy at the AS itself). The architecture has three time
bands:

- Immediate (AS, TTS). On a
  revocation event for a given access token jti or a given (Subject,
  agent) standing delegation, the AS MUST mark the affected token as
  revoked in its token-introspection store, refuse all subsequent `/token`
  Token Exchanges that would re-issue against the same standing
  delegation policy until the policy is reauthorized, and refuse any
  /introspect lookup that returns active for the revoked jti. The TTS
  MUST refuse all subsequent `/txn-token` requests whose subject\_token
  has the revoked jti or has been issued against a revoked standing
  delegation. Both responses MUST emit “refused” audit records per
  Section 8.1.
- Near-real-time (Resource Servers).
  Resource Servers that have already accepted
  access tokens or `Txn-Token`s under the affected jti are not reachable
  through the AS’s introspection store alone. The AS MUST emit a
  Continuous Access Evaluation Profile {{CAEP}} event addressed to all
  Resource Servers in the audience set of the revoked token, containing
  the revoked at\_jti and an event\_type of “session\_revoked.” Resource
  Servers MUST consume CAEP events on a stream they configure with the
  AS at relying-party registration time and MUST honor revocation events
  within an implementation-defined latency budget. Deployments SHOULD
  set the budget at single-digit seconds.
- Eventual (token expiry).
  Even without CAEP, the short-lifetime
  properties of Sections 5.3.2, 6.3, and 7.3 bound the worst-case
  exploitation window of a revoked-but-still-cached token: 10 minutes
  for the SVID, 15 minutes for the delegated AT, 60 seconds for the
  `Txn-Token`. CAEP narrows this to seconds; lifetime alone bounds it to
  minutes. CAEP is RECOMMENDED rather than REQUIRED because not all
  Resource Servers in the relevant ecosystem support CAEP receivers as
  of the publication of this draft.

<aside markdown="1">
**SECURITY GAP**

Gap G-5: Revocation Propagation. If a user revokes a delegation (e.g., via a ‘stop agent’
action in the UI), the revocation signal must reach: (a) the AS
(immediate, addressed by this section), (b) the TTS (immediate,
addressed by this section), and (c) all Resource Servers that have
accepted tokens against the affected access token. (c) is not achievable
with bearer-token architectures alone: it requires either very short
token lifetimes (addressed) or a real-time token revocation mechanism.
CAEP [CAEP] (OpenID Continuous Access Evaluation Profile) provides a
framework for pushing revocation events to Resource Servers in real-time
and is the recommended approach above; until CAEP is universally
deployed across the agent’s likely Resource Servers, the residual gap is
the time between revocation and natural token expiry. This is the AIMS
Monitoring residual gap for this profile.
</aside>

## Session Invalidation Signals {#session-invalidation-signals}

The user-gesture session model defined in
{{OS-Workload-Attestation}} Section 3.3 is invalidated by a defined set
of signals: explicit user dismissal, agent process termination, OS-level
user-absence (screen-lock, session-switch, idle timeout), CAEP receipt,
and elapse of the deployment-defined session ceiling. AIMS Monitoring is
the function that observes these signals and emits the corresponding
audit records (Section 8.1). On any session-invalidation signal, the WIB
MUST emit a “session\_invalidated” record, the AS MUST refuse subsequent
`/token` requests whose actor\_token references the invalidated session
until a fresh user gesture has been collected, and the TTS MUST refuse
subsequent `/txn-token` requests in the same manner.

Session invalidation is the local-trust-domain analog
of CAEP: the same event surface, scoped to the local components,
propagated through the local audit channel rather than over a
network.

## Operator and Subject-Visible Surfaces {#operator-and-subject-visible-surfaces}

AIMS Monitoring serves two distinct audiences:
operators (administrators of the deployment, who consume the audit
channel) and Subjects (the human users whose delegations are being
observed). Both audiences MUST be served, but the surfaces are
distinct:

- Operator surface. Structured
  audit records per Section 8.1, in a format suitable for ingestion by
  SIEM / log-aggregation systems. The operator surface is authoritative;
  audit records MUST NOT be elided or summarized in the operator
  channel.
- Subject surface. A
  Subject-visible activity log accessible from the WIB UI (or an
  analogous credential-management product surface) that displays, in
  human-comprehensible form, the delegations the Subject has issued, the
  agents currently operating under them, and the resources those agents
  have accessed. The Subject surface MAY summarize and SHOULD redact
  internal correlation fields that are not meaningful to the Subject.
  The Subject surface MUST surface revocation as an explicit,
  gesture-confirmed action; revocation issued from this surface MUST
  propagate per Section 8.3.

The Subject surface is what makes AIMS Monitoring
meaningful to the user whose authority is being delegated. A Monitoring
function visible only to operators delegates the Subject’s oversight to
the deployment; this profile requires that the Subject can directly
observe and revoke their own delegations.

# Complete End-to-End Sequence {#complete-end-to-end-sequence}

The following sequence covers the complete lifecycle of
a single local delegated agent task, from human authentication through
resource access, with each phase annotated to the AIMS function it
realizes. The phase enumeration immediately below is the normative
reference. Sequence 9.1, which appears after the phases, is the
illustrative diagram. Where the prose and the diagram disagree (which
they should not), the prose governs.

Phase 1: AIMS Authentication (human leg).

Subject authenticates to the IdP via WebAuthn / FIDO2
per Section 6.1. PKCE-protected OAuth Authorization Code flow yields a
Subject access token bound to the Subject’s identity. The Subject AT is
then delivered from the OAuth client component to the agent’s
credential-handling layer per §6.1, ready for use as subject\_token in
Phase 3.

Phase 2: AIMS Attestation + AIMS Provisioning.

Local Agent connects to the WIB Workload API per
{{OS-Workload-Attestation}} Section 3 and submits a FetchJWTSVID request
naming the requested SPIFFE ID and audience. The WIB performs the
six-step verification of {{OS-Workload-Attestation}} Section 4 against
the connecting peer, surfaces a user gesture if the SPIFFE ID is
high-sensitivity per Section 3.3 of the same document, and on success
mints a JWT-SVID per Section 5.3.2 of this document.

Phase 3: AIMS Authentication (agent leg) + AIMS
Authorization (per-task).

Local Agent presents the WIB-issued SVID as
actor\_token to the AS’s `/token` endpoint, with the Subject’s access
token as subject\_token and a requested scope. The AS validates the SVID
against its enrolled-WIB trust bundle, confirms bound\_subject matches
the subject\_token’s sub, applies graduated trust based on
attest\_methods (Section 4.5 PDP evaluation), enforces scope
attenuation, and mints a delegated access token with sub, `act.sub`, and a
fresh jti per Section 7.1.

Phase 4: Intent capture + per-call AIMS
Authorization.

Subject states the task as a natural-language string.
Local Agent computes intent\_hash per Section 7.4 and POSTs the
delegated AT plus intent\_hash to the TTS’s `/txn-token` endpoint. The TTS
validates the AT, runs PDP evaluation against runtime context (Section
4.5), and mints a `Txn-Token` per Section 7.3 carrying sub, `actor.sub`,
at\_jti, intent\_hash, and tool\_call.

Phase 5: Tool execution + AIMS Monitoring.

Local Agent invokes the Resource Server with the
delegated AT in the Authorization header and the `Txn-Token` in the
`Txn-Token` header. The Resource Server PEP validates both artifacts,
enforces the requested action against the granted scope, and emits a
structured audit record per Section 8.1 carrying at\_jti, txn, sub,
`act.sub`, resource, and action. The cycle of Phase 4 + Phase 5 repeats
for each tool call within the agent’s task; a fresh `Txn-Token` is minted
per call. Phase 5’s audit emissions are the input to the AIMS Monitoring
function for the entire task.

<figure anchor="fig-1">
<name>Figure 1</name>
<artwork type="ascii-art" align="center">
@@IMG:assets/images/local-delegated/image1.png@@
</artwork>
</figure>

Sequence 9.1: Complete local delegated agent flow.
Phase 1: human authentication. Phase 2: WIB attestation and JWT-SVID
provisioning. Phase 3: per-task delegated AT issuance at the AS. Phase
4: per-call `Txn-Token` issuance with intent binding at the TTS. Phase 5:
resource invocation, scope enforcement, and audit emission. Phases 4 and
5 repeat for each tool call within the agent’s task; a fresh `Txn-Token`
is minted per call.

# Security Considerations and Gaps {#security-considerations-and-gaps}

This section enumerates the security properties of the
local delegated agent architecture and identifies specific gaps that are
not fully addressed by currently available standards. Each gap is tagged
for cross-reference. Gaps are organized by the AIMS function whose
realization they affect, so an implementer or reviewer can scope their
analysis to a specific function.

## Authentication Security Properties {#authentication-security-properties}

### Phishing Resistance {#phishing-resistance}

WebAuthn {{WebAuthn-L3}} with origin binding ensures
that the human Subject’s credential cannot be replayed to a fraudulent
IdP. The FIDO2 authenticator signs the challenge bound to the relying
party’s registered origin; a phishing site at a different origin cannot
obtain a valid assertion. This property holds for both native local
agents (which open the OS browser for authentication) and
browser-sandbox agents (where the WebAuthn ceremony is origin-bound to
the application). This is the AIMS Authentication property that makes
delegation trustworthy at the human leg.

### Agent-Identity Anchoring {#agent-identity-anchoring}

The agent’s authentication to the AS does not rely on a
long-lived agent-held key. Instead, agent identity is anchored in the
WIB-issued JWT-SVID, which the AS validates against its enrolled-WIB
trust bundle. The SVID itself is the proof of agent identity. It could
only have been minted by a WIB that holds a key in its platform secure
key store (Apple Secure Enclave, Windows TPM, or equivalent) AND only
after the WIB performed the per-issuance peer verification of
{{OS-Workload-Attestation}} Section 4. The security property substituted
for client-held proof-of-possession is per-issuance binary attestation
by the WIB, anchored in OS code-signing.

## Authorization Security Properties {#authorization-security-properties}

### Scope Attenuation {#scope-attenuation}

The Token Exchange MUST enforce that the delegated
access token’s scope is a strict subset of the Subject’s access token
scope. In typical delegation scenarios, the Subject may hold broad
privileges across many resources, but the agent is issued a token scoped
exclusively to the specific operation and resource it requires. This
ensures the agent cannot acquire more authority than the user explicitly
delegated. See Gap G-2.

### Temporal Bounding {#temporal-bounding}

All agent credentials are short-lived (15-minute AT,
60-second `Txn-Token`s, 10-minute SVID). This limits the window of
exploitation in the event of credential theft. REQUIREMENT:
Implementations MUST NOT issue refresh tokens for agent-scoped access
tokens. Temporal bounding is an AIMS Credentials property, but its
enforcement responsibility sits at the AIMS Authorization layer (which
mints the tokens) and the AIMS Monitoring layer (which observes their
use).

### Per-Call Replay Window {#per-call-replay-window}

Without sender-constraining (DPoP, mTLS, or another
proof-of-possession mechanism) on the delegated access token, a captured
AT could in principle be replayed by an attacker for the remainder of
the AT’s lifetime. This profile relies on three layered properties to
bound that window:

- The AT alone is not sufficient to invoke a Resource
  Server; a fresh `Txn-Token` from the TTS is also required (Section 7.2).
  An attacker holding a stolen AT must also obtain a `Txn-Token` under it,
  which requires presenting the AT to the TTS (which validates against
  the AS’s revocation state, Section 8.3).
- The `Txn-Token` has a 60-second lifetime and carries an
  immutable identity context, so even a successful TTS request yields
  only a 60-second per-call window.
- CAEP-mediated revocation propagation (Section 8.3)
  shrinks the worst-case AT exploitation window from the AT’s natural
  15-minute lifetime to single-digit seconds in deployments where
  Resource Servers consume CAEP.

The residual risk is the time between AT theft and
either (a) revocation propagation reaching the TTS or (b) AT natural
expiry, whichever is shorter. Future revisions of this document, or
companion specifications, may add proof-of-possession on the AT layer;
see Section 12.

### Delegation Revocation {#delegation-revocation}

See Section 8.3 for the revocation propagation
mechanism and Gap G-5 for the residual gap.

## Prompt Injection Mitigation {#prompt-injection-mitigation}

Prompt injection is a first-order threat for local
delegated agents. An attacker who can influence the content returned by
a tool call (e.g., a malicious SQL result payload, query response, or
injected schema comment) may embed instructions that cause the LLM to
take actions outside the user’s declared intent.

Current mitigations available in this architecture,
organized by the AIMS function each leverages:

- Intent Binding (AIMS Authorization, Section
  7.4) ties the `Txn-Token` to a specific hash of
  the user’s intent. Actions that meaningfully deviate from the intent
  hash can be flagged by PDP policy.
- `Txn-Token` scope binding (AIMS
  Authorization): the tctx claim’s tool\_call
  field SHOULD enumerate authorized tool types. The PDP SHOULD refuse to
  issue `Txn-Token`s for tool calls not consistent with the declared
  tool\_call envelope.
- Short `Txn-Token` lifetimes (AIMS
  Credentials): a compromised `Txn-Token` has a
  maximum 60-second exploitation window.
- Human-in-the-loop re-authorization (AIMS
  Authentication): for high-sensitivity actions
  (e.g., write operations to production systems), the agent SHOULD
  surface a confirmation prompt requiring the Subject to actively
  approve, triggering a new WebAuthn ceremony.
- Real-time CAEP signaling (AIMS Monitoring, Section
  8.3): when prompt-injection-attributable
  behavior is detected by an upstream observer, CAEP propagates the
  revocation to all Resource Servers within the latency budget of
  Section 8.3.

<aside markdown="1">
**SECURITY GAP**

Gap G-6: No Standardized Prompt Injection Detection
Protocol. There is no IETF or W3C standard for a
‘prompt injection detection’ signal that an agent runtime can include in
a `Txn-Token` request to attest that tool outputs have been scanned. The
draft NIST AIMS concept paper [NIST-AIMS] identifies this as an open
area. Until standardized, implementations MUST apply defense-in-depth:
(1) tool output content filtering, (2) strict scope constraints, (3)
minimal toolset enrollment per delegation, and (4) anomaly detection at
the PDP layer. See also [AI-AUTH] Section 10 for the AI-Auth draft’s
treatment of prompt injection.
</aside>

## Local Trust Boundary Specific Risks {#local-trust-boundary-specific-risks}

### Memory Scraping and Token Exfiltration {#memory-scraping-and-token-exfiltration}

Other processes running as the same OS user can read
the agent’s process memory, potentially extracting in-memory access
tokens or `Txn-Token`s. This is a threat to the AIMS Credentials function
in the local trust domain. Mitigations:

- Bound the exposure window via the short token
  lifetimes of Section 10.2.2 (15-minute AT, 60-second Txn-Token, 10-minute SVID).
- Apply OS-level process isolation and ASLR; enforce
  code signing on the agent binary so the WIB’s peer verification
  (Section 5.2.4) refuses to issue SVIDs to tampered or replaced agent
  processes.
- Minimize the lifetime of tokens in agent memory: the
  agent SHOULD discard tokens immediately after the request that uses
  them rather than caching them across the AT’s natural lifetime.
- The WIB’s own device-bound key is protected by the
  platform secure key store (Apple Secure Enclave, Windows TPM, or
  equivalent) and is not loaded into application-accessible memory; see
  {{OS-Workload-Attestation}} for the WIB’s self-protection
  requirements.

<aside markdown="1">
**SECURITY GAP**

Gap G-7: Residual Binary Attestation Gap on
Consumer Devices. The Workload Identity Broker
pattern (Section 5.2) substantially narrows the binary-attestation gap
by anchoring agent identity in code-signing verification performed by a
hardened, AS-enrolled local daemon, rather than allowing any process
running as the user to self-assert an agent identity. To impersonate a
verified agent, an attacker must subvert one of: (a) the OS code-signing
subsystem, (b) the WIB’s allowlist population channel (vendor manifest,
MDM policy, or user opt-in), or (c) the WIB itself; each of these is
substantially harder than the baseline of executing a process under the
same OS user account. However, on consumer (non-MDM) devices, the WIB’s
own enrollment cannot leverage hardware-rooted device attestation (Tier
1, Section 5.2.2) and falls back to user-anchored enrollment (Tier 2).
The AS SHOULD apply graduated trust based on the SVID’s attest_methods
claim (Section 5.3.2). For example, the AS may reduce scope ceilings or
require more frequent re-attestation for SVIDs whose attest_methods
array does not include hardware attestation. This is the AIMS
Attestation residual gap for this profile. RESOLUTION PATH: TPM 2.0
Measured Boot + Remote Attestation ({{RATS-ARCH}} RFC 9334) on managed
devices closes this gap for the enterprise tier; the consumer tier
remains a residual gap.
</aside>

### Browser-Sandbox Specific Risks {#browser-sandbox-specific-risks}

- Cross-origin information leakage:
  Agent WIMSE IDs embedded in HTTP headers must
  not be leaked to cross-origin iframes or third-party scripts.
  REQUIREMENT: Authorization and `Txn-Token` headers MUST NOT be included
  in cross-origin requests.
- Service worker interception:
  A malicious service worker can intercept fetch
  requests and exfiltrate tokens. REQUIREMENT: The browser-sandbox agent
  MUST NOT operate in origins that permit untrusted service worker
  registration.
- DOM-based prompt injection:
  Rendered web content (e.g., AI-summarized
  emails) can inject instructions into agent prompts if not sanitized.
  REQUIREMENT: All agent inputs derived from rendered DOM MUST be
  treated as untrusted and passed through a content sanitization layer
  before LLM context inclusion.

# Comparison: Local vs. Remote Delegated Agent {#comparison-local-vs-remote-delegated-agent}

The following table summarizes the key differences
between the local delegated architecture (this document) and the remote
delegated architecture (doc 2 of 6). Both are AIMS reference
architectures and use the same AIMS Authorization wire format (Token
Exchange with act claim); they differ primarily in which mechanism
realizes AIMS Attestation, where AIMS Credentials are stored, and the
trust-boundary characteristics that shape the AIMS Monitoring
function.

| AIMS function or property | Local Delegated | Remote Delegated |
|---|---|---|
| Execution environment | End-user device / browser | Cloud-managed container / VM |
| AIMS Attestation realization | OS code-signing via WIB ([OS-Workload-Attestation] §4); not hardware-rooted by default (Gap G-7) | Workload Identity Federation with cloud-platform identity issuer; SPIFFE / SPIRE + TEE available |
| Agent credential storage | WIB device key in OS secure key store / Secure Enclave / TPM; agent itself holds no long-lived key in this revision | HSM or cloud KMS; mTLS client cert per workload |
| AT proof-of-possession | None in this revision; per-call binding via `Txn-Token` | mTLS client certificate bound to AT (when [WIMSE-S2S] is used) |
| TTS location | Remote (cross-trust-domain) | Within remote trust domain |
| Human in loop | Present; FIDO2 consent feasible per task | Absent; delegation pre-authorized via ID-JAG |
| `Txn-Token` issuance | Cross-boundary (higher latency) | Same-domain (lower latency) |
| Prompt injection risk | Higher (local tool outputs) | Moderate (controlled tool outputs) |
| Refresh tokens | MUST NOT issue | SHOULD NOT; short-lived AT + rotation |

# Out of Scope and Future Work {#out-of-scope-and-future-work}

This revision is deliberately scoped to capabilities
that exist in shipping or actively-drafted specifications today. The
following items were considered during development and excluded; they
are listed here so that an implementer or reviewer can locate work that
has been deferred rather than abandoned, and so that the boundary
between this reference architecture and the work that follows it is
explicit.

- Vendor-specific delegation identifier (dlg\_id).
  Earlier drafts of this document defined a
  custom dlg\_id JWT claim to anchor each delegation event distinctly
  from the access token’s jti. Karl McGuinness’s review (see Acknowledgments)
  observed that this is a custom mechanism deserving its own
  specification rather than a paragraph in a profile document. This
  revision uses the standard JWT jti and the `Txn-Token`’s txn for
  correlation (Section 5.4 and Section 8.2). A future companion
  specification may define richer delegation semantics and how to convey
  them across token types; that work is not part of this
  document.
- Proof-of-possession on the delegated access token.
  Earlier drafts bound the delegated AT to an
  agent-held DPoP key per {{RFC9449}}. This revision does not, on the
  principle that the architecture should be grounded only in
  capabilities that exist in shipping specifications without requiring
  the agent to manage long-lived asymmetric key material in the local
  trust domain. The per-call binding properties that DPoP provided are
  now provided by the `Txn-Token` layer (Section 7.3, Section 10.2.3).
  Adding sender-constraining to the AT, via DPoP, mTLS, or another
  mechanism, is appropriate future work for deployments that need to
  defend against AT theft within the AT’s lifetime more aggressively
  than CAEP-mediated revocation provides. Such an addition would be
  additive to this profile and would not invalidate conformance.
- Attenuating tokens for sub-agent delegation.
  Sub-agent flows (where one agent invokes
  another) are addressed in companion documents 3 through 6 of this
  series (the bounded and autonomous profiles). Recent IETF work on
  attenuating authorization tokens
  (draft-niyikiza-oauth-attenuating-agent-tokens-00) is relevant prior
  art and will be evaluated in those documents.
- Capability-declaration system for intent binding.
  Section 7.4’s intent\_hash binds the `Txn-Token`
  to a user-declared natural-language goal but does not mechanically
  constrain agent tool calls (Gap G-3). A capability declaration system
  in which the agent’s allowed tools are pre-enrolled and the `Txn-Token`
  only authorizes specific declared capabilities would close that gap.
  Such a system is not yet standardized; it is anticipated future work
  in the {{AI-AUTH}} track.
- Externalized PDP wire protocol.
  Section 4.5 specifies the PDP’s position and
  inputs but does not define a wire protocol for an externalized PDP.
  Deployments that externalize the PDP today use deployment-specific
  transports. A standardized PDP-consultation protocol is potential
  future work.

--- back

# Acknowledgments
{:numbered="false"}

The authors thank the following individuals for review, feedback, and prior art that materially shaped this document:

Karl McGuinness for the architectural review that prompted the scope tightening reflected in this revision: specifically, the recommendation to separate the interoperable AIMS reference architecture from vendor-specific extensions, to ground the document in shipping or actively-drafted specifications, and to make the Policy Decision Point's role explicit (Section 4.5).

Nick Steele (OpenAI; co-author of {{AI-AUTH}}) for substantive discussion of the AIMS model and its application to local-execution agent profiles.

The authors of {{AI-AUTH}} / draft-klrc-aiagent-auth: Pieter Kasselman (Defakto Security), Jean-François Lombardo (AWS), Yaroslav Rosomakho (Zscaler), Brian Campbell (Ping Identity), and Nick Steele (OpenAI), whose elaboration of the AIMS conceptual model is the immediate parent of the function definitions used throughout this document. The mapping in Section 4.4 follows their seven-function decomposition; any errors of application are the responsibility of the authors of this document.

The authors of {{NIST-AIMS}} at the NIST National Cybersecurity Center of Excellence, whose concept paper introduced the AIMS framing that this document realizes for the local-delegated profile.

Acknowledgment does not imply endorsement; the named individuals reviewed material, contributed prior art, or co-authored upstream specifications that this document depends on. Responsibility for the contents of this document rests with the listed authors.

# About This Document
{:numbered="false"}

1Password Research & Development

<https://1password.com/security>

Document series: `draft-1password-agent-identity-local-delegated-00`, Part 1 of 6

Companion: draft-1password-os-level-workload-attestation-00 (AIMS Attestation + Provisioning realization)

Next document: draft-1password-agent-identity-remote-delegated-00 (AIMS reference architecture for the remote-delegated profile)
