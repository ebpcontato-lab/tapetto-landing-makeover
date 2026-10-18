<!-- LOVABLE:BEGIN -->
> [!IMPORTANT]
> This project is connected to [Lovable](https://lovable.dev). Avoid rewriting
> published git history — force pushing, or rebasing/amending/squashing commits
> that are already pushed — as it rewrites history on Lovable's side and the
> user will likely lose their project history.
>
> Commits you push to the connected branch sync back to Lovable and show up in
> the editor, so keep the branch in a working state.
<!-- LOVABLE:END -->

- Keep the Tapetto page static; uploaded media uses CDN asset pointers, and standalone exports resolve these to local assets so they work on any static host.
- Keep the static landing template; quote submissions call a dedicated same-origin TanStack server route backed by an INSERT-only Cloud table so visitors cannot read customer data. Saving requests requires the hosted service, not a standalone static host.
- Send quote notifications through the server-only notification module after a successful new insert, using the fixed recipient and event-derived idempotency key; email failures must preserve the saved request, and duplicate IDs must not resend altered data. Never create an email queue or claim delivery before sending succeeds.
- Keep the landing form's submit usable on a plain static host: when the save endpoint is unreachable or answers without JSON, offer the WhatsApp handoff with the composed message instead of claiming the order was saved; only a JSON error from the real backend shows a failure message.
