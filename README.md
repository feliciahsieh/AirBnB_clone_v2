<h1 class="gap">0x03. AirBnB clone - Deploy static</h1>


<h4 class="task">
    0. Prepare your web servers
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a Bash script that sets up your web servers for the deployment of <code>web_static</code>. It must:</p><ul>
<li>Install Nginx if it not already installed</li>
<li>Create the folder <code>/data/</code> if it doesn’t already exist</li>
<li>Create the folder <code>/data/web_static/</code> if it doesn’t already exist</li>
<li>Create the folder <code>/data/web_static/releases/</code> if it doesn’t already exist</li>
<li>Create the folder <code>/data/web_static/shared/</code> if it doesn’t already exist</li>
<li>Create the folder <code>/data/web_static/releases/test/</code> if it doesn’t already exist</li>
<li>Create a fake HTML file <code>/data/web_static/releases/test/index.html</code> (with simple content, to test your Nginx configuration)</li>
<li>Create a symbolic link <code>/data/web_static/current</code> linked to the <code>/data/web_static/releases/test/</code> folder. If the symbolic link already exists, it should be deleted and recreated every time the script is ran.</li>
<li>Give ownership of the <code>/data/</code> folder to the <code>ubuntu</code> user AND group (you can assume this user and group exist). This should be recursive; everything inside should be created/owned by this user/group.</li>
<li>Update the Nginx configuration to serve the content of <code>/data/web_static/current/</code> to <code>hbnb_static</code> (ex: <code>https://mydomainname.tech/hbnb_static</code>). Don’t forget to restart Nginx after updating the configuration:

<ul>
<li>Use <code>alias</code> inside your Nginx configuration</li>
<li><a href="/rltoken/kGBgDBs1rNj_N3eyy5juYA" target="_blank" title="Tip">Tip</a></li>
</ul></li>
</ul><p>Your program should always exit successfully.
<strong>Don’t forget to run your script on both of your web servers.</strong></p><p>In optional, you will redo this task but by using Puppet</p>


<h4 class="task">
    1. Compress before sending
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a Fabric script that generates a <a href="/rltoken/Y2c7VhkIhpTf3O4W-IYRRQ" target="_blank" title=".tgz">.tgz</a> archive from the contents of the <code>web_static</code> folder of your AirBnB Clone repo, using the function <code>do_pack</code>.</p><ul>
<li>Prototype: <code>def do_pack():</code></li>
<li>All files in the folder <code>web_static</code> must be added to the final archive</li>
<li>All archives must be stored in the folder <code>versions</code> (your function should create this folder if it doesn’t exist)</li>
<li>The name of the archive created must be <code>web_static_&lt;year&gt;&lt;month&gt;&lt;day&gt;&lt;hour&gt;&lt;minute&gt;&lt;second&gt;.tgz</code></li>
<li>The function <code>do_pack</code> must return the archive path if the archive has been correctly generated. Otherwise, it should return <code>None</code></li>
</ul>


<h4 class="task">
    2. Deploy archive!
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a Fabric script (based on the file <code>1-pack_web_static.py</code>) that distributes an archive to your web servers, using the function <code>do_deploy</code>:</p><ul>
<li>Prototype: <code>def do_deploy(archive_path):</code></li>
<li>Returns <code>False</code> if the file at the path <code>archive_path</code> doesn’t exist</li>
<li>The script should take the following steps:

<ul>
<li>Upload the archive to the <code>/tmp/</code> directory of the web server</li>
<li>Uncompress the archive to the folder <code>/data/web_static/releases/&lt;archive filename without extension&gt;</code> on the web server</li>
<li>Delete the archive from the web server</li>
<li>Delete the symbolic link <code>/data/web_static/current</code> from the web server</li>
<li>Create a new the symbolic link <code>/data/web_static/current</code> on the web server, linked to the new version of your code (<code>/data/web_static/releases/&lt;archive filename without extension&gt;</code>)</li>
</ul></li>
<li>All remote commands must be executed on your both web servers (using <code>env.hosts = ['&lt;IP web-01&gt;', 'IP web-02']</code> variable in your script)</li>
<li>Returns <code>True</code> if all operations has been done correctly, otherwise returns <code>False</code></li>
</ul><p>In the following example, the SSH key and the username used for accessing to the server are passed in the command line. Of course, you could define them as Fabric environment variables (ex: <code>env.user =...</code>)</p>


<h4 class="task">
    3. Full deployment
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a Fabric script (based on the file <code>2-do_deploy_web_static.py</code>) that creates and distributes an archive to your web servers, using the function <code>deploy</code>:</p><ul>
<li>Prototype: <code>def deploy():</code></li>
<li>The script should take the following steps:

<ul>
<li>Call the <code>do_pack()</code> function and store the path of the created archive</li>
<li>Return <code>False</code> if no archive has been created</li>
<li>Call the <code>do_deploy(archive_path)</code> function, using the new path of the new archive</li>
<li>Return the return value of <code>do_deploy</code></li>
</ul></li>
<li>All remote commands must be executed on both of web your servers (using <code>env.hosts = ['&lt;IP web-01&gt;', 'IP web-02']</code> variable in your script)</li>
</ul><p>In the following example, the SSH key and the username used for accessing to the server are passed in the command line. Of course, you could define them as Fabric environment variables (ex: env.user =…)</p>


<h4 class="task">
    4. Keep it clean!
      <span class="alert alert-info mandatory-optional">
        #advanced
      </span>
</h4><p>Write a Fabric script (based on the file <code>3-deploy_web_static.py</code>) that deletes out-of-date archives, using the function <code>do_clean</code>:</p><ul>
<li>Prototype: <code>def do_clean(number=0):</code></li>
<li><code>number</code> is the number of the archives, including the most recent, to keep.

<ul>
<li>If <code>number</code> is 0 or 1, keep only the most recent version of your archive. </li>
<li>if <code>number</code> is 2, keep the most recent, and second most recent versions of your archive.</li>
<li>etc.</li>
</ul></li>
<li>Your script should:

<ul>
<li>Delete all unnecessary archives (all archives minus the number to keep) in the <code>versions</code> folder</li>
<li>Delete all unnecessary archives (all archives minus the number to keep) in the <code>/data/web_static/releases</code> folder of both of your web servers</li>
</ul></li>
<li>All remote commands must be executed on both of your web servers (using the <code>env.hosts = ['&lt;IP web-01&gt;', 'IP web-02']</code> variable in your script)</li>
</ul><p>In the following example, the SSH key and the username used for accessing to the server are passed in the command line. Of course, you could define them as Fabric environment variables (ex: env.user =…)</p>


<h4 class="task">
    5. Puppet for setup
      <span class="alert alert-info mandatory-optional">
        #advanced
      </span>
</h4><p>Redo the task #0 but by using Puppet:</p>

